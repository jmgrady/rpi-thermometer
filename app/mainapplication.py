import argparse
import sys
from typing import Optional

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication
from baseui import BaseUi
from graphicalui import GraphicalUi
from sensors.basesensor import BaseSensor


class MainApplication(QApplication):
    def __init__(self, args: argparse.Namespace):
        super().__init__(sys.argv)

        # Create application components
        self.ui: Optional[BaseUi] = None
        self.sensor: Optional[BaseSensor] = None
        if args.target == "rpi":
            if args.ui == "gui":
                self.ui = GraphicalUi(self)
                self.ui.quit_request.connect(self.quit)
            else:
                self.ui = BaseUi(self)

            from sensors.spitempsensor import SpiTempSensor

            self.sensor = SpiTempSensor(self)
        else:
            self.ui = BaseUi(self)
            self.sensor = BaseSensor(self)
        self.timer = QTimer(self)

        # Connect the components
        if self.sensor is not None and self.ui is not None:
            self.timer.timeout.connect(self.sensor.start_measurement)
            self.sensor.meas_complete.connect(self.ui.update_value)

    def start(self) -> None:
        self.timer.start(5000)
