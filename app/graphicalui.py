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
        self.window = MainWindow()  # type: ignore[no-untyped-call]
        self.window.ui.actionQuit.triggered.connect(self.send_quit)
        self.window.show()
        self.start()
        self.units = "F"

    @Slot()
    def start(self) -> None:
        super(GraphicalUi, self).start()
        self.start_time = datetime.now()
        self.window.ui.tempValue.setText("- ? -")

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
