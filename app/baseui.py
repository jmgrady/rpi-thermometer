from datetime import datetime
import logging
import math
from typing import Optional

from PySide6.QtCore import QObject, Signal, Slot


class BaseUi(QObject):
    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)
        self.temp_value = str(math.nan)
        self.start_time = datetime.now()

    quit_request = Signal()
    start_measurements = Signal(int)
    stop_measurements = Signal()

    @Slot(str, float)
    def update_value(self, timestamp: str, value_str: str) -> None:
        logging.debug(f"New measurement: ({timestamp}, {value_str})")
        self.temp_value = value_str
