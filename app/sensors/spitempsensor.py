from datetime import datetime
import logging
from typing import List, Optional

from PySide6.QtCore import QObject, Slot
import adafruit_max31865
import board
import digitalio
from sensors.basesensor import BaseSensor


class SpiTempSensor(BaseSensor):
    spi_channels = (digitalio.DigitalInOut(board.D5), digitalio.DigitalInOut(board.D6))

    def __init__(self, num_channels: int, parent: Optional[QObject] = None):
        self.sensor_list: List[adafruit_max31865.MAX31865] = []
        super(BaseSensor, self).__init__(parent)
        if num_channels < 0 or num_channels > len(self.spi_channels):
            logging.error(f"Invalid number of channels requested: {num_channels}")
        else:
            for ix in range(num_channels):
                self.sensor_list.append(
                    adafruit_max31865.MAX31865(
                        board.SPI(),
                        self.spi_channels[ix],
                        rtd_nominal=100,
                        ref_resistor=430,
                        wires=3,
                    )
                )
                logging.info(f"Creating SpiTempSensor for channel {ix}")

    @Slot()
    def start_measurement(self) -> None:
        timestamp = str(datetime.now())
        temperature_list: List[float] = []
        for ix in range(len(self.sensor_list)):
            temperature_list.append(self.sensor_list[ix].temperature)

        value_str = ";".join(map(str, temperature_list))
        self.meas_complete.emit(f"{timestamp}", value_str)
        logging.info(f"{timestamp}: emitted value {value_str}")
