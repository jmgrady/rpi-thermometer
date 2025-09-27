from datetime import datetime, timedelta
import logging
import math
from typing import List, Optional

from PySide6.QtCore import QObject, Slot, QThreadPool
from appconfig import app_config, Units
from baseui import BaseUi
from mainwindow import MainWindow
from savedataagent import SaveDataAgent
from settingsdialog import SettingsDialog

"""
To Do:
Create a separate object to save the data.  It will manage whether a save dialog is
displayed or not and will manage the background worker thread.
"""


class GraphicalUi(BaseUi):

    def __init__(self, parent: Optional[QObject] = None):
        super(GraphicalUi, self).__init__(parent)
        self.reset()
        self.window = MainWindow()  # type: ignore[no-untyped-call]
        self.init_ui()
        self.settings_dlg = SettingsDialog()
        self.save_data_agent = SaveDataAgent(self.window)
        self.connect_signals()
        self.window.show()
        self.meas_times: List[float] = []
        self.meas_values: List[float] = []
        self.threadpool = QThreadPool()

    def connect_signals(self) -> None:
        self.window.ui.actionQuit.triggered.connect(self.send_quit)
        self.window.ui.actionSave.triggered.connect(self.save_results)
        self.window.ui.actionSave_As.triggered.connect(self.save_results_as)
        self.window.ui.actionSettings.triggered.connect(self.on_settings)
        self.window.ui.startButton.clicked.connect(self.on_start_clicked)
        self.window.ui.stopButton.clicked.connect(self.on_stop_clicked)

    def init_ui(self) -> None:
        self.window.ui.tempValue.setText("- ? -")
        self.window.ui.elapsedTimeValue.setText(f"{timedelta(0)}")
        self.window.ui.graphWindow.clear()
        self.meas_times = []
        self.meas_values = []

    def save_results_as(self) -> None:
        self.save_data_agent.save(
            self.meas_times,
            self.meas_values,
            auto_save_file=False,
            gui=True,
        )

    def save_results(self) -> None:
        self.save_data_agent.save(
            self.meas_times,
            self.meas_values,
            auto_save_file=True,
            gui=True,
        )

    def send_quit(self) -> None:
        self.quit_request.emit()

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
            self.meas_times.append(elapsed_time.total_seconds())
            self.meas_values.append(scaled_value)
            self.window.ui.graphWindow.plot(self.meas_times, self.meas_values)

    @Slot()
    def on_start_clicked(self) -> None:
        self.reset()
        self.init_ui()
        self.window.ui.startButton.setDisabled(True)
        self.window.ui.stopButton.setDisabled(False)
        # Start the timer for periodic measurements
        self.start_measurements.emit(app_config.sample_period_msec())

    @Slot()
    def on_stop_clicked(self) -> None:
        self.stop_measurements.emit()
        self.window.ui.startButton.setDisabled(False)
        self.window.ui.stopButton.setDisabled(True)

    @Slot()
    def on_settings(self) -> None:
        self.settings_dlg.show()
