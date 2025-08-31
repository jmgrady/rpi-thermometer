from datetime import datetime
import logging
import math
from typing import Optional

from PySide6.QtCore import QObject, Signal, Slot


class BaseUi(QObject):
    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)
        self.start_time = datetime.now()
        self.temp_value = math.nan

    quit_request = Signal()

    @Slot()
    def start(self) -> None:
        self.start_time = datetime.now()
        self.temp_value = math.nan
        logging.info(f"Start time set to {self.start_time}")

    @Slot(str, float)
    def update_value(self, timestamp: str, value: float) -> None:
        logging.debug(f"New measurement: ({timestamp}, {value})")
        self.temp_value = value
