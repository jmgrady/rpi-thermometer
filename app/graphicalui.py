from dataclasses import dataclass
from datetime import datetime, timedelta
import logging
import math
from typing import Dict, List, Optional

from PySide6.QtCore import QObject, QThreadPool, Slot, Qt
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
        self.meas: Dict[str, MeasSeries] = {}
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
        self.window.ui.tempValue.setText("- ? -")
        self.window.ui.elapsedTimeValue.setText(f"{timedelta(0)}")
        self.window.ui.graphWindow.setBackground("#e0e0e0")
        self.window.ui.graphWindow.clear()
        self.meas = {}

    def save_results_as(self) -> None:
        self.save_data_agent.save(
            self.meas["raw"].times,
            self.meas["raw"].values,
            auto_save_file=False,
            gui=True,
        )

    def save_results(self) -> None:
        self.save_data_agent.save(
            self.meas["raw"].times,
            self.meas["raw"].values,
            auto_save_file=True,
            gui=True,
        )

    def send_quit(self) -> None:
        self.quit_request.emit()

    def average_samples(self, samples: List[float], num_samples: int) -> float:
        return sum(samples[-num_samples:]) / num_samples

    def add_sample(self, series_name: str, elapsed_sec: float, value: float) -> None:
        if series_name not in self.meas:
            self.meas[series_name] = MeasSeries([elapsed_sec], [value])
        else:
            self.meas[series_name].times.append(elapsed_sec)
            self.meas[series_name].values.append(value)

    def update_graph(
        self,
        series_name: str,
        *,
        pen: QPen,
        symbol: Optional[str] = None,
        symbol_size: Optional[int] = None,
        symbol_brush: Optional[QBrush] = None,
    ) -> None:
        if series_name in self.data_lines:
            self.data_lines[series_name].setData(
                self.meas[series_name].times, self.meas[series_name].values
            )
        else:
            self.data_lines[series_name] = self.window.ui.graphWindow.plot(
                self.meas[series_name].times,
                self.meas[series_name].values,
                pen=pen,
                symbol=symbol,
                symbolSize=symbol_size,
                symbolBrush=symbol_brush,
            )

    @Slot(str, float)
    def update_value(self, timestamp: str, value: float) -> None:
        elapsed_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f") - self.start_time
        logging.info(f"({elapsed_time.total_seconds()}, {value})")

        # round elapsed time to the nearest second
        elapsed_time = timedelta(seconds=int(elapsed_time.total_seconds()))
        self.window.ui.elapsedTimeValue.setText(f"{elapsed_time}")

        # update the temperature value
        if math.isnan(value):
            self.window.ui.tempValue.setText("- ? -")
        else:
            if app_config.units() == Units.DEG_F:
                scaled_value = value * 9.0 / 5.0 + 32.0
            else:
                scaled_value = value
            self.window.ui.tempValue.setText(f"{scaled_value:.1f} °{app_config.units().value}")
            if self.recording:
                # Update the plot line for the instantaneous ("raw") measurement
                self.add_sample("raw", elapsed_time.total_seconds(), scaled_value)
                self.update_graph("raw", pen=pg.mkPen(255, 0, 0))

                # Plot the running average
                running_avg_count = min(
                    len(self.meas["raw"].values),
                    int(app_config.averaging_time() / app_config.sample_period()),
                )
                running_avg = self.average_samples(self.meas["raw"].values, running_avg_count)
                self.add_sample("avg", elapsed_time.total_seconds(), running_avg)
                self.update_graph("avg", pen=pg.mkPen(0, 0, 255))

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
            self.add_sample("mark", self.meas["raw"].times[-1], self.meas["raw"].values[-1])
            self.update_graph(
                "mark",
                pen=QPen(Qt.PenStyle.NoPen),
                symbol="|",
                symbol_size=25,
                symbol_brush=pg.mkBrush((0, 128, 0)),
            )
