from datetime import datetime, timedelta
import logging
import math
from typing import Dict, List, Optional

from PySide6.QtCore import QObject, QThreadPool, Slot
from appconfig import Units, app_config
from baseui import BaseUi
from datatypes import Measurements
from graphconfig import get_brush, get_pen
from mainwindow import MainWindow
import pyqtgraph as pg
from savedataagent import SaveDataAgent
from settingsdialog import SettingsDialog


class GraphicalUi(BaseUi):

    def __init__(self, parent: Optional[QObject] = None):
        super(GraphicalUi, self).__init__(parent)
        self.window = MainWindow()  # type: ignore[no-untyped-call]
        self.data: Dict[str, Measurements] = {
            "raw": Measurements([], []),
            "avg": Measurements([], []),
            "mark": Measurements([], []),
        }
        self.init_ui()
        self.settings_dlg = SettingsDialog()
        self.save_data_agent = SaveDataAgent(self.window)
        self.connect_signals()
        self.window.show()
        self.threadpool = QThreadPool()
        self.recording = False
        self.num_chan = app_config.num_channels()
        self.data_lines: List[Dict[str, Optional[pg.PlotDataItem.PlotDataItem]]] = []
        for _ in range(self.num_chan):
            self.data_lines.append({"raw": None, "avg": None, "mark": None})
        logging.info(f"self.meas keys: {self.data.keys()}")

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
        self.data["raw"] = Measurements([], [])
        self.data["avg"] = Measurements([], [])

    def save_results_as(self) -> None:
        self.save_data_agent.save(
            self.data["raw"],
            auto_save_file=False,
            gui=True,
        )

    def save_results(self) -> None:
        self.save_data_agent.save(
            self.data["raw"],
            auto_save_file=True,
            gui=True,
        )

    def send_quit(self) -> None:
        self.quit_request.emit()

    def average_samples(self, samples: List[float], num_samples: int) -> float:
        return sum(samples[-num_samples:]) / num_samples

    def add_sample(self, series_name: str, elapsed_sec: float, values: List[float]) -> None:
        if series_name not in self.data:
            logging.error(f"Unrecognized data series, {series_name}")
        else:
            self.data[series_name].times.append(elapsed_sec)
            self.data[series_name].values.extend(values)

    def update_graph(
        self,
        series_name: str,
        *,
        symbol: Optional[str] = None,
        symbol_size: Optional[int] = None,
    ) -> None:
        for channel in range(self.num_chan):
            if self.data_lines[channel][series_name] is not None:
                plot_data_item: pg.PlotDataItem.PlotDataItem = self.data_lines[channel][
                    series_name
                ]
                plot_data_item.setData(
                    self.data[series_name].times,
                    self.data[series_name].values[channel :: self.num_chan],
                )
            else:
                logging.info(f"Keys of self.meas: {self.data.keys()}")
                self.data_lines[channel][series_name] = self.window.ui.graphWindow.plot(
                    self.data[series_name].times,
                    self.data[series_name].values[channel :: self.num_chan],
                    pen=get_pen(series_name, channel),
                    symbol=symbol,
                    symbolSize=symbol_size,
                    symbolBrush=get_brush(series_name),
                )

    def set_value_label(self, channel: int, text: str) -> None:
        if channel == 0:
            self.window.ui.tempValue_0.setText(text)
        else:
            self.window.ui.tempValue_1.setText(text)

    @Slot(str, int, float)
    def update_value(self, timestamp: str, value_str: str) -> None:

        value_list = list(map(float, value_str.split(";")))

        if len(value_list) <= self.num_chan and len(value_list) > 0:
            elapsed_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f") - self.start_time
            logging.info(f"({elapsed_time.total_seconds()}, {value_list})")

            # round elapsed time to the nearest second
            elapsed_time = timedelta(seconds=int(elapsed_time.total_seconds()))
            self.window.ui.elapsedTimeValue.setText(f"{elapsed_time}")

            # update the temperature values
            scaled_value_list: List[float] = []
            for channel in range(self.num_chan):
                if math.isnan(value_list[channel]):
                    self.set_value_label(channel, "- ? -")
                    scaled_value_list.append(value_list[channel])
                else:
                    if app_config.units() == Units.DEG_F:
                        scaled_value_list.append(value_list[channel] * 9.0 / 5.0 + 32.0)
                    else:
                        scaled_value_list.append(value_list[channel])
                    self.set_value_label(
                        channel, f"{scaled_value_list[channel]:.1f} °{app_config.units().value}"
                    )

            if self.recording:
                # Update the plot line for the instantaneous ("raw") measurement
                self.add_sample("raw", elapsed_time.total_seconds(), scaled_value_list)
                self.update_graph(
                    "raw",
                )

                # Plot the running averages
                running_avgs: List[float] = []
                for channel in range(self.num_chan):
                    averaging_sample_set: List[float] = self.data["raw"].values[
                        channel :: self.num_chan
                    ]
                    running_avg_count = min(
                        len(averaging_sample_set),
                        int(app_config.averaging_time() / app_config.sample_period()),
                    )
                    running_avgs.append(
                        self.average_samples(averaging_sample_set, running_avg_count)
                    )
                self.add_sample("avg", elapsed_time.total_seconds(), running_avgs)
                self.update_graph(
                    "avg",
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

        if "raw" in self.data:
            self.add_sample(
                "mark",
                self.data["raw"].times[-1],
                self.data["raw"].values[-self.num_chan :],
            )
            self.update_graph(
                "mark",
                symbol="|",
                symbol_size=25,
            )
