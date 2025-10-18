from datetime import datetime
import logging
from typing import Optional

from PySide6.QtCore import QObject, Slot
import adafruit_max31865
import board
import digitalio
from sensors.basesensor import BaseSensor


class SpiTempSensor(BaseSensor):
    spi_channels = (digitalio.DigitalInOut(board.D5), digitalio.DigitalInOut(board.D26))

    def __init__(self, channel_number: int, parent: Optional[QObject] = None):
        super(BaseSensor, self).__init__(parent)
        if channel_number < 0 or channel_number >= len(self.spi_channels):
            logging.error(f"Invalid channel number requested: {channel_number}")
            self.sensor = None
        else:
            chip_select = self.spi_channels[channel_number]
            chip_select.direction = digitalio.Direction.INPUT
            chip_select.pull = digitalio.Pull.UP
            self.sensor = adafruit_max31865.MAX31865(
                board.SPI(), chip_select, rtd_nominal=100, ref_resistor=400, wires=3
            )

    @Slot()
    def start_measurement(self) -> None:
        if self.sensor is not None:
            timestamp = datetime.now()
            self.meas_complete.emit(f"{timestamp}", self.sensor.temperature)
