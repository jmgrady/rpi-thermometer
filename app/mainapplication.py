import argparse
import sys
from typing import Optional

from PySide6.QtCore import QTimer, Slot
from PySide6.QtWidgets import QApplication
from appconfig import AppConfig, Sensors
from baseui import BaseUi
from graphicalui import GraphicalUi
from sensors.basesensor import BaseSensor
from sensors.mocksensor import MockSensor


class MainApplication(QApplication):
    def __init__(self, args: argparse.Namespace):
        super().__init__(sys.argv)

        # Create application components
        self.ui: Optional[BaseUi] = None
        self.sensor: Optional[BaseSensor] = None
        self.config = AppConfig("PiProjects", "RPi Thermometer")

        sample_period_sec = float(self.config.sample_period())
        self.sample_period_msec = int(sample_period_sec * 1000.0)

        # Instantiate the selected UI mode
        if args.ui == "gui":
            self.ui = GraphicalUi(self.config, self)
            self.ui.quit_request.connect(self.quit)
            self.ui.start_measurements.connect(self.start_timer)
            self.ui.stop_measurements.connect(self.stop_timer)
        else:
            self.ui = BaseUi(self)

        # Instantiate the selected sensors
        sensor_type = self.config.sensor_type()
        if sensor_type == Sensors.SPI:

            from sensors.spitempsensor import SpiTempSensor

            self.sensor = SpiTempSensor(self)
        elif sensor_type == Sensors.SIM:
            self.sensor = MockSensor(self)

        # Create the timer to trigger measurements
        self.timer = QTimer(self)

        # Connect the components
        if self.sensor is not None and self.ui is not None:
            self.timer.timeout.connect(self.sensor.start_measurement)
            self.sensor.meas_complete.connect(self.ui.update_value)

    @Slot()
    def start_timer(self) -> None:
        self.timer.start(self.sample_period_msec)

    @Slot()
    def stop_timer(self) -> None:
        self.timer.stop()
