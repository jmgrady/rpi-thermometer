#! /usr/bin/env python3

import argparse
import logging
import sys

from mainapplication import MainApplication


def parse_args() -> argparse.Namespace:
    """Parse user command line arguments."""
    parser = argparse.ArgumentParser(
        description="Parse options for temperature logging.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--mode",
        "-m",
        choices=["quiet", "info", "debug"],
        default="info",
        help="Select the logging mode",
    )
    parser.add_argument(
        "--period",
        "-p",
        help="Period (in seconds) between temperature measurements.",
        default=15.0,
    )
    parser.add_argument(
        "--target", choices=["rpi", "host"], default="rpi", help="Specify runtime target"
    )
    parser.add_argument(
        "--ui",
        choices=["gui", "serial"],
        default="gui",
        help="Specify mode for displaying the measured temperature.",
    )
    return parser.parse_args()


def init_log_level(args: argparse.Namespace) -> None:
    if args.mode == "debug":
        log_level = logging.DEBUG
    elif args.mode == "quiet":
        log_level = logging.WARNING
    else:
        log_level = logging.INFO
    logging.basicConfig(format="%(levelname)s:%(message)s", level=log_level)


if __name__ == "__main__":
    args = parse_args()
    init_log_level(args)
    app = MainApplication(args)

    sys.exit(app.exec())
