import logging
from pathlib import Path
import sys
import traceback
from typing import List

from PySide6.QtCore import (
    QObject,
    QRunnable,
    Signal,
    Slot,
)


class WorkerSignals(QObject):
    """Signals from a running worker thread.

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc())

    progress
        float indicating % progress
    """

    finished = Signal()
    error = Signal(tuple)
    progress = Signal(float)


class SaveDataWorker(QRunnable):
    """Worker thread.

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread.
                     Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function
    """

    def __init__(
        self,
        meas_times: List[float],
        meas_values: List[float],
        output_path: Path,
    ):
        super().__init__()
        self.meas_times = meas_times
        self.meas_values = meas_values
        self.output_path = output_path
        self.signals = WorkerSignals()
        # Add the callbacks to our kwargs
        self.killed = False

    @Slot()
    def run(self) -> None:
        try:
            with open(self.output_path, "w") as output_file:
                for i in range(0, len(self.meas_times) - 1):
                    if self.killed:
                        logging.info("Worker Thread canceled.")
                        break
                    output_file.write(f"{self.meas_times[i]}\t{self.meas_values[i]}\n")
                    if i % 10 == 0:
                        self.signals.progress.emit(100.0 * (i / len(self.meas_times)))
        except Exception:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        finally:
            self.signals.finished.emit()

    @Slot()
    def kill(self) -> None:
        self.killed = True
