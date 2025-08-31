from dataclasses import dataclass

from adafruit_blinka.microcontroller.bcm283x import pin
import digitalio


@dataclass(frozen=True)
class LedColor:
    r: bool
    g: bool
    b: bool


class RgbLed:
    off = LedColor(False, False, False)
    red = LedColor(True, False, False)
    green = LedColor(False, True, False)
    blue = LedColor(False, False, True)
    yellow = LedColor(True, True, False)
    cyan = LedColor(False, True, True)
    magenta = LedColor(True, False, True)
    white = LedColor(True, True, True)

    def __init__(self, r_pin: pin, g_pin: pin, b_pin: pin) -> None:
        self.red_led = digitalio.DigitalInOut(r_pin)
        self.red_led.direction = digitalio.Direction.OUTPUT
        self.red_led.value = False
        self.green_led = digitalio.DigitalInOut(g_pin)
        self.green_led.direction = digitalio.Direction.OUTPUT
        self.green_led.value = False
        self.blue_led = digitalio.DigitalInOut(b_pin)
        self.blue_led.direction = digitalio.Direction.OUTPUT
        self.blue_led.value = False

    def set_color(self, color: LedColor) -> None:
        self.red_led.value = color.r
        self.green_led.value = color.g
        self.blue_led.value = color.b
