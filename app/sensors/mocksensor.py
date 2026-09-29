from datetime import datetime
import logging
import random
from typing import List, Optional

from PySide6.QtCore import QObject, Slot
from sensors.basesensor import BaseSensor


class MockSensor(BaseSensor):
    def __init__(self, num_channels: int, parent: Optional[QObject]):
        super(BaseSensor, self).__init__(parent)
        self.num_channels = num_channels
        self.current_values: List[float] = []
        for _ix in range(num_channels):
            self.current_values.append(65.0)

    @Slot()
    def start_measurement(self) -> None:
        timestamp = str(datetime.now())
        logging.debug(f"{timestamp}: BaseSensor.start_measurement()")
        for ix in range(self.num_channels):
            self.current_values[ix] += (random.random() * 5.0) - 2.5
        self.meas_complete.emit(f"{timestamp}", ";".join(map(str, self.current_values)))
