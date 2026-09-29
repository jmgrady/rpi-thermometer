from datetime import datetime
import logging
from typing import Optional

from PySide6.QtCore import QObject, Signal, Slot


class BaseSensor(QObject):
    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)

    # Signal arguments are (timestamp, measurements)
    # measurements is a ';' delimited string of list of measurements
    meas_complete = Signal(str, str)

    @Slot()
    def start_measurement(self) -> None:
        timestamp = str(datetime.now())
        logging.debug(f"{timestamp}: BaseSensor.start_measurement()")
        self.meas_complete.emit(timestamp, "0.0")
