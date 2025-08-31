from datetime import datetime
from typing import Optional

from PySide6.QtCore import QObject, Slot
import adafruit_max31865
import board
import digitalio
from sensors.basesensor import BaseSensor


class SpiTempSensor(BaseSensor):
    def __init__(self, parent: Optional[QObject]):
        super(BaseSensor, self).__init__(parent)
        chip_select = digitalio.DigitalInOut(board.D5)
        chip_select.direction = digitalio.Direction.INPUT
        chip_select.pull = digitalio.Pull.UP
        self.sensor = adafruit_max31865.MAX31865(
            board.SPI(), chip_select, rtd_nominal=100, ref_resistor=400, wires=3
        )

    @Slot()
    def start_measurement(self) -> None:
        timestamp = datetime.now()
        self.meas_complete.emit(f"{timestamp}", self.sensor.temperature)
