from datetime import datetime, timedelta
import logging
import math
from typing import Optional

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
        if math.isnan(value):
            self.window.ui.tempValue.setText("- ? -")
        else:
            if self.units == "F":
                self.window.ui.tempValue.setText(f"{value * 9.0 / 5.0 + 32.0:.1f} °F")
            else:
                self.window.ui.tempValue.setText(f"{value:.1f} °C")
        # round elapsed time to the nearest second
        elapsed_time = timedelta(seconds=int(elapsed_time.total_seconds()))
        self.window.ui.elapsedTimeValue.setText(f"{elapsed_time}")

    @Slot()
    def on_start_clicked(self) -> None:
        self.reset()
        self.start_measurements.emit()

    @Slot()
    def on_stop_clicked(self) -> None:
        self.stop_measurements.emit()
