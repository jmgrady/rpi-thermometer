from datetime import datetime
import logging
from typing import Optional

from PySide6.QtCore import QObject, Signal, Slot


class BaseSensor(QObject):
    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)

    # Signal arguments are (timestamp, measurement)
    # timestamp is the time in seconds from self.base_tine
    meas_complete = Signal(str, float)

    @Slot()
    def start_measurement(self) -> None:
        timestamp = datetime.now()
        logging.debug(f"{timestamp}: BaseSensor.start_measurement()")
        self.meas_complete.emit(timestamp, 0.0)
