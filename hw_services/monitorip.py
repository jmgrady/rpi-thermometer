#! /usr/bin/env python3

from ipaddress import IPv4Address
import logging
import re
import sys
import time
from typing import Optional, Tuple

import board
from chardisplay import CharDisplay
import digitalio
from utils import run_cmd


def get_network_name(type: str) -> Tuple[Optional[str], Optional[str]]:
    results = run_cmd(["nmcli", "c", "show", "--active"])
    net_connections = results.stdout.split("\n")
    for connection in net_connections:
        cx_fields = re.split(" +", connection)
        if len(cx_fields) >= 4 and cx_fields[2] == type:
            return (cx_fields[0], cx_fields[3])
    return (None, None)


def get_dev_ip(dev: Optional[str]) -> Optional[IPv4Address]:
    if dev is not None:
        results = run_cmd(["ip", "address", "show", dev])
        for line in results.stdout.split("\n"):
            match = re.match(r" +inet ([\d\.]+)", line)
            if match is not None:
                return IPv4Address(match.group(1))
    return None


class IpDisplay:
    """Class to display the IP address on a character display."""

    def __init__(
        self,
        display_select: digitalio.DigitalInOut,
        disp_name: str,
        *,
        num_cols: int = 16,
        num_rows: int = 2,
        refresh_period: float = 1.0,
    ):
        self.l_display_select = display_select  # active low
        self.display_name = disp_name
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.refresh_period = refresh_period

    def run(self, *, if_type: str) -> None:
        while True:
            if not self.l_display_select.value:
                (netname, device) = get_network_name(if_type)
                logging.debug(f"Network Name: {netname}")
                ip_addr = get_dev_ip(device)
                logging.debug(f"IP {ip_addr}")
                display = CharDisplay(self.display_name, self.num_cols, self.num_rows)
                if display is not None:
                    # Move cursor to origin
                    display.to_origin()
                    if ip_addr is not None and netname is not None:
                        display.set_background(CharDisplay.GREEN)
                        display.write(netname, pad=True)
                        display.move(1, 2)
                        display.write("    ")
                        display.write(f"IP: {ip_addr}", pad=True)
                    else:
                        display.set_background(CharDisplay.RED)
                        display.write("NO ETHERNET", pad=True)
                        display.move(1, 2)
                        display.write("    ")
                        display.write("AVAILABLE", pad=True)
                    display.close()
            time.sleep(self.refresh_period)


if __name__ == "__main__":
    gpio_pin = digitalio.DigitalInOut(board.D22)
    gpio_pin.direction = digitalio.Direction.INPUT
    gpio_pin.pull = digitalio.Pull.UP
    ip_display = IpDisplay(gpio_pin, "/dev/ttyACM0", refresh_period=0.5)
    try:
        ip_display.run(if_type="wifi")
    except KeyboardInterrupt:
        sys.exit(0)
