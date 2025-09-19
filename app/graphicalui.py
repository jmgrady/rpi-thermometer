from datetime import datetime, timedelta
import logging
import math
from pathlib import Path
from typing import List, Optional

from PySide6.QtCore import QObject, Slot
from PySide6.QtWidgets import QFileDialog
from appconfig import AppConfig, Units
from baseui import BaseUi
from mainwindow import MainWindow
from settingsdialog import SettingsDialog


class GraphicalUi(BaseUi):

    def __init__(self, config: AppConfig, parent: Optional[QObject] = None):
        super(GraphicalUi, self).__init__(parent)
        self.config = config
        self.settings_dlg = SettingsDialog(self.config)
        self.reset()
        self.window = MainWindow()  # type: ignore[no-untyped-call]
        self.init_ui()
        self.connect_signals()
        self.window.show()
        self.meas_times: List[float] = []
        self.meas_values: List[float] = []

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

    def write_results_file(self, output_path: Path) -> None:
        logging.info(f"Saving to {output_path}")
        with open(output_path, "w") as output_file:
            for i in range(0, len(self.meas_times) - 1):
                output_file.write(f"{self.meas_times[i]}\t{self.meas_values[i]}\n")

    def save_results_as(self) -> None:
        dialog = QFileDialog(self.window)
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        dialog.setDefaultSuffix("tsv")
        dialog.setDirectory(str(self.config.save_dir()))
        dialog.setNameFilter("*.tsv *.csv")
        if dialog.exec():
            filenames = dialog.selectedFiles()
            self.write_results_file(Path(filenames[0]).resolve())
        else:
            logging.info("Saving canceled")

    def save_results(self) -> None:
        basefilename = (
            f"{self.start_time.year}-{self.start_time.month:02d}-{self.start_time.day:02d}-"
            f"{self.start_time.hour:02d}:{self.start_time.minute:02d}:"
            f"{self.start_time.second:02d}.tsx"
        )
        save_dir = self.config.save_dir()
        self.write_results_file(save_dir / basefilename)

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
            if self.config.units() == Units.DEG_F:
                scaled_value = value * 9.0 / 5.0 + 32.0
            else:
                scaled_value = value
            self.window.ui.tempValue.setText(f"{scaled_value:.1f} °{self.config.units().value}")
            self.meas_times.append(elapsed_time.total_seconds())
            self.meas_values.append(scaled_value)
            self.window.ui.graphWindow.plot(self.meas_times, self.meas_values)

    @Slot()
    def on_start_clicked(self) -> None:
        self.reset()
        self.init_ui()
        self.window.ui.startButton.setDisabled(True)
        self.window.ui.stopButton.setDisabled(False)
        self.start_measurements.emit()

    @Slot()
    def on_stop_clicked(self) -> None:
        self.stop_measurements.emit()
        self.window.ui.startButton.setDisabled(False)
        self.window.ui.stopButton.setDisabled(True)

    @Slot()
    def on_settings(self) -> None:
        self.settings_dlg.show()
