#! /usr/bin/env python3

import argparse
from datetime import datetime
from enum import Enum, unique
import logging
import sys
import time
from typing import Optional

import adafruit_max31865
import board
from chardisplay import CharDisplay
import digitalio


@unique
class LoggingState(Enum):
    IDLE = "idle"
    LOGGING = "logging"


class TemperatureLogger:
    def __init__(
        self,
        disp_name: str,
        *,
        display_select: digitalio.DigitalInOut,
        chip_select: digitalio.DigitalInOut,
        meas_period: float,
    ):
        self.l_display_select = display_select  # active low
        self.display_name = disp_name
        self.spi = board.SPI()
        self.cs = chip_select
        self.state = LoggingState.IDLE
        self.meas_period = meas_period
        self.log_filename = ""
        self.log_switch = digitalio.DigitalInOut(board.D6)
        self.log_switch.direction = digitalio.Direction.INPUT
        self.log_switch.pull = digitalio.Pull.UP
        self.logging_indicator = digitalio.DigitalInOut(board.D19)
        self.logging_indicator.direction = digitalio.Direction.OUTPUT
        self.logging_indicator.value = False

    def get_display(self) -> Optional[CharDisplay]:
        if not self.l_display_select.value:
            return CharDisplay(self.display_name, 16, 2)
        return None

    def display_temp(self, temp_c: float, temp_f: float, timestamp: datetime) -> None:
        display = self.get_display()
        if display is not None:
            if temp_f > 160:
                bg_color = CharDisplay.RED
            elif temp_f > 145:
                bg_color = CharDisplay.GREEN
            else:
                bg_color = CharDisplay.CYAN
            # Display it on the screen.
            display.set_background(bg_color)
            display.to_origin()
            display.write(f"{timestamp.astimezone().strftime('%H:%M:%S')}", pad=True, newline=True)
            display.move(1, 2)
            display.write("    ")
            display.write(f"{temp_c:5.1f} C  {temp_f:5.1f} F", pad=True)
            display.close()

    def run(self, sample_rate: float = 1.0) -> None:
        max31865 = adafruit_max31865.MAX31865(
            self.spi, self.cs, rtd_nominal=100, ref_resistor=400, wires=3
        )
        while True:
            timestamp = datetime.now()
            time_str = timestamp.astimezone().strftime("%Y-%m-%d %H:%M:%S")
            temp_c = max31865.temperature
            temp_f = temp_c * 9 / 5 + 32
            self.display_temp(temp_c, temp_f, timestamp)
            if self.log_switch.value:
                self.logging_indicator.value = True
                if self.state == LoggingState.IDLE:
                    self.log_filename = (
                        f"data/Temp_log_{timestamp.astimezone().strftime('%Y-%m-%d_%H_%M_%S')}"
                    )
                    self.state = LoggingState.LOGGING
                logging.debug(f"{time_str}\t{temp_c:5.1f}\t{temp_f:5.1f}")
                with open(self.log_filename, "a") as logfile:
                    logfile.write(f"{time_str}\t{temp_c:5.1f}\t{temp_f:5.1f}\n")
            else:
                self.logging_indicator.value = False
                self.state = LoggingState.IDLE
            exec_time = (datetime.now() - timestamp).total_seconds()
            sleep_time = self.meas_period - exec_time
            if sleep_time > 0:
                time.sleep(sleep_time)


def parse_args() -> argparse.Namespace:
    """Parse user command line arguments."""
    parser = argparse.ArgumentParser(
        description="Parse options for temperature logging.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--period",
        help="Period (in seconds) between temperature measurements.",
        default=15.0,
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    display_select = digitalio.DigitalInOut(board.D27)
    display_select.direction = digitalio.Direction.INPUT
    display_select.pull = digitalio.Pull.UP
    chip_select = digitalio.DigitalInOut(board.D5)
    chip_select.direction = digitalio.Direction.INPUT
    chip_select.pull = digitalio.Pull.UP
    temperature_logger = TemperatureLogger(
        "/dev/ttyACM0",
        display_select=display_select,
        chip_select=chip_select,
        meas_period=args.period,
    )
    try:
        temperature_logger.run()
    except KeyboardInterrupt:
        sys.exit(0)
