from dataclasses import dataclass
from datetime import datetime, timedelta
import logging
import math
from typing import Dict, List, Optional

from PySide6.QtCore import QObject, Qt, QThreadPool, Slot
from PySide6.QtGui import QBrush, QPen
from appconfig import Units, app_config
from baseui import BaseUi
from mainwindow import MainWindow
import pyqtgraph as pg
from savedataagent import SaveDataAgent
from settingsdialog import SettingsDialog


@dataclass
class MeasSeries:
    times: List[float]
    values: List[float]


class GraphicalUi(BaseUi):

    def __init__(self, parent: Optional[QObject] = None):
        super(GraphicalUi, self).__init__(parent)
        self.window = MainWindow()  # type: ignore[no-untyped-call]
        self.init_ui()
        self.settings_dlg = SettingsDialog()
        self.save_data_agent = SaveDataAgent(self.window)
        self.connect_signals()
        self.window.show()
        self.meas: Dict[str, List[MeasSeries]] = {"raw": [], "avg": []}
        for _ix in range(app_config.num_channels()):
            self.meas["raw"].append(MeasSeries([], []))
            self.meas["avg"].append(MeasSeries([], []))
        self.threadpool = QThreadPool()
        self.recording = False
        self.data_lines: Dict[str, pg.PlotDataItem.PlotDataItem] = {}

    def connect_signals(self) -> None:
        self.window.ui.actionQuit.triggered.connect(self.send_quit)
        self.window.ui.actionSave.triggered.connect(self.save_results)
        self.window.ui.actionSave_As.triggered.connect(self.save_results_as)
        self.window.ui.actionSettings.triggered.connect(self.on_settings)
        self.window.ui.graphButton.clicked.connect(self.on_graph_button_clicked)
        self.window.ui.addMarkButton.clicked.connect(self.on_add_mark_button_clicked)

    def set_button_status(self) -> None:
        self.window.ui.addMarkButton.setEnabled(self.recording)

    def init_ui(self) -> None:
        self.window.ui.tempValue_0.setText("- ? -")
        self.window.ui.tempValue_1.setText("- ? -")
        self.window.ui.elapsedTimeValue.setText(f"{timedelta(0)}")
        self.window.ui.graphWindow.setBackground("#e0e0e0")
        self.window.ui.graphWindow.clear()
        self.meas = {}

    def save_results_as(self) -> None:
        self.save_data_agent.save(
            self.meas["raw"][0].times,
            self.meas["raw"][0].values,
            auto_save_file=False,
            gui=True,
        )

    def save_results(self) -> None:
        self.save_data_agent.save(
            self.meas["raw"][0].times,
            self.meas["raw"][0].values,
            auto_save_file=True,
            gui=True,
        )

    def send_quit(self) -> None:
        self.quit_request.emit()

    def average_samples(self, samples: List[float], num_samples: int) -> float:
        return sum(samples[-num_samples:]) / num_samples

    def add_sample(self, series_name: str, channel: int, elapsed_sec: float, value: float) -> None:
        if series_name not in self.meas:
            logging.error(f"Unrecognized data series, {series_name}")
        else:
            self.meas[series_name][channel].times.append(elapsed_sec)
            self.meas[series_name][channel].values.append(value)

    def update_graph(
        self,
        series_name: str,
        channel: int,
        *,
        pen: QPen,
        symbol: Optional[str] = None,
        symbol_size: Optional[int] = None,
        symbol_brush: Optional[QBrush] = None,
    ) -> None:
        if series_name in self.data_lines:
            self.data_lines[series_name][channel].setData(
                self.meas[series_name][channel].times, self.meas[series_name][channel].values
            )
        else:
            self.data_lines[series_name][channel] = self.window.ui.graphWindow.plot(
                self.meas[series_name][channel].times,
                self.meas[series_name][channel].values,
                pen=pen,
                symbol=symbol,
                symbolSize=symbol_size,
                symbolBrush=symbol_brush,
            )

    def set_value_label(self, channel: int, text: str) -> None:
        if channel == 0:
            self.window.ui.tempValue_0.setText(text)
        else:
            self.window.ui.tempValue_1.setText(text)

    @Slot(str, float)
    def update_value(self, timestamp: str, channel: int, value: float) -> None:

        if channel < app_config.num_channels() and channel >= 0:
            elapsed_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f") - self.start_time
            logging.info(f"({elapsed_time.total_seconds()}, {channel}, {value})")

            # round elapsed time to the nearest second
            elapsed_time = timedelta(seconds=int(elapsed_time.total_seconds()))
            self.window.ui.elapsedTimeValue.setText(f"{elapsed_time}")

            # update the temperature value
            if math.isnan(value):
                self.set_value_label(channel, "- ? -")
            else:
                if app_config.units() == Units.DEG_F:
                    scaled_value = value * 9.0 / 5.0 + 32.0
                else:
                    scaled_value = value
                self.set_value_label(channel, f"{scaled_value:.1f} °{app_config.units().value}")

                if self.recording:
                    # Update the plot line for the instantaneous ("raw") measurement
                    self.add_sample("raw", channel, elapsed_time.total_seconds(), scaled_value)
                    self.update_graph(
                        "raw", channel, pen=pg.mkPen(color=app_config.get_color("raw", channel))
                    )

                    # Plot the running average
                    running_avg_count = min(
                        len(self.meas["raw"][channel].values),
                        int(app_config.averaging_time() / app_config.sample_period()),
                    )
                    running_avg = self.average_samples(
                        self.meas["raw"][channel].values, running_avg_count
                    )
                    self.add_sample("avg", channel, elapsed_time.total_seconds(), running_avg)
                    self.update_graph(
                        "avg", channel, pen=pg.mkPen(color=app_config.get_color("avg", channel))
                    )

    @Slot()
    def on_graph_button_clicked(self) -> None:
        if self.recording:
            self.recording = False
        else:
            self.recording = True
            self.start_time = datetime.now()
            self.init_ui()
        self.set_button_status()

    @Slot()
    def on_settings(self) -> None:
        self.settings_dlg.show()

    @Slot()
    def on_add_mark_button_clicked(self) -> None:
        logging.info(f"Mark set at {datetime.now()}")

        if "raw" in self.meas:
            for channel in range(app_config.num_channels()):
                self.add_sample(
                    "mark",
                    channel,
                    self.meas["raw"][channel].times[-1],
                    self.meas["raw"][channel].values[-1],
                )
            self.update_graph(
                "mark",
                channel,
                pen=QPen(Qt.PenStyle.NoPen),
                symbol="|",
                symbol_size=25,
                symbol_brush=pg.mkBrush(color=app_config.get_color("mark", channel)),
            )
