import logging

import serial


class CharDisplay:
    RED = bytearray(b"\xff\x00\x00")
    GREEN = bytearray(b"\x00\xff\x00")
    BLUE = bytearray(b"\x00\x00\xff")
    YELLOW = bytearray(b"\xff\xff\x00")
    MAGENTA = bytearray(b"\xff\x00\xff")
    CYAN = bytearray(b"\x00\xff\xff")
    WHITE = bytearray(b"\xff\xff\xff")
    BLACK = bytearray(b"\x00\x00\x00")

    def __init__(self, tty_name: str, num_cols: int, num_rows: int):
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.ser = serial.Serial(
            tty_name,
            9600,
            bytesize=serial.EIGHTBITS,
            stopbits=serial.STOPBITS_ONE,
            parity=serial.PARITY_NONE,
            xonxoff=False,
            rtscts=False,
        )
        self.ser.flushInput()
        self.ser.flushOutput()

        self.addr = None

    def write(self, buffer: str, *, pad: bool = False, newline: bool = False) -> None:
        if pad:
            padded_buffer = buffer.center(self.num_cols)
            logging.debug(f"Padded Buffer: {padded_buffer}")
            self.ser.write(padded_buffer.encode(encoding="ascii"))
        else:
            self.ser.write(bytes(buffer, "ascii"))
        if newline:
            self.ser.write(b"\x0a")
        self.ser.flushOutput()

    def clear_screen(self) -> None:
        self.ser.write(bytearray(b"\xfe\x58"))
        self.ser.flushOutput()

    def to_origin(self) -> None:
        self.ser.write(bytearray(b"\xfe\x48"))
        self.ser.flushOutput()

    def move(self, column: int, row: int) -> None:
        if column < self.num_cols and row < self.num_rows:
            self.ser.write(bytearray(b"\xfe\x47"))
            self.ser.write(bytearray(column.to_bytes()))
            self.ser.write(bytearray(row.to_bytes()))
            self.ser.write(bytearray(b"\x0a"))
            self.ser.flushOutput()

    def set_background(self, color: bytearray) -> None:
        self.ser.write(bytearray(b"\xfe\xd0"))
        self.ser.write(color)
        self.ser.flushOutput()

    def close(self) -> None:
        self.ser.flushOutput()
        self.ser.close()
