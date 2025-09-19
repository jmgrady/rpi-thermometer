from datetime import datetime
import logging
import random
from typing import Optional

from PySide6.QtCore import QObject, Slot
from sensors.basesensor import BaseSensor


class MockSensor(BaseSensor):
    def __init__(self, parent: Optional[QObject]):
        super(BaseSensor, self).__init__(parent)
        self.current_value = 65.0

    @Slot()
    def start_measurement(self) -> None:
        timestamp = datetime.now()
        logging.debug(f"{timestamp}: BaseSensor.start_measurement()")
        self.current_value += (random.random() * 5.0) - 2.5
        self.meas_complete.emit(f"{timestamp}", self.current_value)
