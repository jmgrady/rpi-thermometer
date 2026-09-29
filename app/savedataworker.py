import logging
from pathlib import Path
import sys
import traceback

from PySide6.QtCore import QObject, QRunnable, Signal, Slot
from appconfig import app_config
from datatypes import Measurements


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
        data: Measurements,
        output_path: Path,
    ):
        super().__init__()
        self.data = data
        self.output_path = output_path
        self.signals = WorkerSignals()
        # Add the callbacks to our kwargs
        self.killed = False

    @Slot()
    def run(self) -> None:
        """
        This function writes the data out to the results file.  It ASSUMES that the number of
        samples is the same for all channels.
        """
        try:
            total_lines = len(self.data.times)
            curr_line = 0
            with open(self.output_path, "w") as output_file:
                for i in range(0, len(self.data.times)):
                    if self.killed:
                        logging.info("Worker Thread canceled.")
                        break
                    output_file.write(f"{self.data.times[i]}")
                    for j in range(
                        i * app_config.num_channels(), (i + 1) * app_config.num_channels()
                    ):
                        output_file.write(f"\t{self.data.values[j]}")
                    output_file.write("\n")
                    curr_line += 1
                    if curr_line % 10 == 0:
                        self.signals.progress.emit(100.0 * (curr_line / total_lines))
        except Exception:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        finally:
            self.signals.finished.emit()

    @Slot()
    def kill(self) -> None:
        self.killed = True
