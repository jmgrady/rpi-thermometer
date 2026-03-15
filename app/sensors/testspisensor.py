#! /usr/bin/env python

import argparse
from datetime import datetime
import time

import adafruit_max31865
import board
import digitalio


def parse_args() -> argparse.Namespace:
    """Parse user command line arguments."""
    parser = argparse.ArgumentParser(
        description="Parse options for temperature logging.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--channel", "-c", choices=["0", "1"], default="0", help="SPI Channel number"
    )
    parser.add_argument(
        "--fahrenheit", "-f", action="store_true", help="Display results in degrees Fahrenheit"
    )
    parser.add_argument(
        "--period",
        "-p",
        help="Period (in seconds) between temperature measurements.",
    )
    return parser.parse_args()


if __name__ == "__main__":

    args = parse_args()

    if args.channel == "1":
        chip_select = digitalio.DigitalInOut(board.D26)
    else:
        chip_select = digitalio.DigitalInOut(board.D5)

    chip_select.direction = digitalio.Direction.INPUT
    chip_select.pull = digitalio.Pull.UP
    sensor = adafruit_max31865.MAX31865(
        board.SPI(), chip_select, rtd_nominal=100, ref_resistor=400, wires=3
    )
    while True:
        dev_value = sensor.temperature
        if args.fahrenheit:
            scaled_value = dev_value * 9.0 / 5.0 + 32.0
            units = "°F"
        else:
            scaled_value = dev_value
            units = "°C"
        print(f"{datetime.now()}: {scaled_value:.2f}{units}")
        if args.period is not None:
            time.sleep(args.period)
        else:
            break
