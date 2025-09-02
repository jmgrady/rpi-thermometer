from datetime import datetime, timedelta
import logging
import math
from typing import List, Optional

from PySide6.QtCore import QObject, Slot
from baseui import BaseUi
from mainwindow import MainWindow


class GraphicalUi(BaseUi):

    def __init__(self, parent: Optional[QObject] = None):
        super(GraphicalUi, self).__init__(parent)
        self.reset()
        self.window = MainWindow()  # type: ignore[no-untyped-call]
        self.init_ui()
        self.window.show()
        self.units = "F"
        self.meas_times: List[float] = []
        self.meas_values: List[float] = []

    def init_ui(self) -> None:
        self.window.ui.actionQuit.triggered.connect(self.send_quit)
        self.window.ui.startButton.clicked.connect(self.on_start_clicked)
        self.window.ui.stopButton.clicked.connect(self.on_stop_clicked)
        self.window.ui.tempValue.setText("- ? -")
        self.window.ui.elapsedTimeValue.setText(f"{timedelta(0)}")

    def send_quit(self) -> None:
        self.quit_request.emit()

    @Slot(str, float)
    def update_value(self, timestamp: str, value: float) -> None:
        elapsed_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f") - self.start_time
        logging.info(f"Elapsed time: {elapsed_time.total_seconds()}")

        # round elapsed time to the nearest second
        elapsed_time = timedelta(seconds=int(elapsed_time.total_seconds()))
        self.window.ui.elapsedTimeValue.setText(f"{elapsed_time}")

        # update the temperature value
        if math.isnan(value):
            self.window.ui.tempValue.setText("- ? -")
        else:
            if self.units == "F":
                scaled_value = value * 9.0 / 5.0 + 32.0
            else:
                scaled_value = value
            self.window.ui.tempValue.setText(f"{scaled_value:.1f} °{self.units}")
            self.meas_times.append(elapsed_time.total_seconds())
            self.meas_values.append(scaled_value)
            self.window.ui.graphWindow.plot(self.meas_times, self.meas_values)

    @Slot()
    def on_start_clicked(self) -> None:
        self.reset()
        self.start_measurements.emit()

    @Slot()
    def on_stop_clicked(self) -> None:
        self.stop_measurements.emit()
