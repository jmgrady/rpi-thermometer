#! /usr/bin/env python3
"""
Check the power button and poweroff if pressed.

Note: Pressing the button a second time will NOT power the
raspberry pi back up; you need to remove and re-apply power.
"""

import os
import time

from adafruit_debouncer import Debouncer
import board
import digitalio
from rgbled import RgbLed


def main() -> None:
    # setup to poweroff switch
    power_gpio_pin = digitalio.DigitalInOut(board.D16)
    power_gpio_pin.direction = digitalio.Direction.INPUT
    power_gpio_pin.pull = digitalio.Pull.UP
    power_switch = Debouncer(power_gpio_pin)
    # setup the indicator LED
    status_led = RgbLed(board.D25, board.D24, board.D23)
    status_led.set_color(RgbLed.blue)

    while True:
        power_switch.update()
        if power_switch.fell:
            status_led.set_color(RgbLed.red)
            os.system("sudo poweroff")
        time.sleep(0.25)


if __name__ == "__main__":
    main()
