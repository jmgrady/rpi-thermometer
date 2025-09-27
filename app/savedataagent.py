"""
Agent to manage saving the collected data in a file.  When its save() method is
invoked, an argument indicates whether it will prompt for a file name or create one
automatically.  The data will be saved in a separate thread. A dialog box to show
the progress may be requested in the save request.
"""

from datetime import datetime
import logging
from pathlib import Path
from typing import List, Optional

from appconfig import app_config
from PySide6.QtCore import QObject, Signal, QThreadPool
from PySide6.QtWidgets import QWidget, QDialog, QFileDialog
from savedataworker import SaveDataWorker
from saveprogressdialog import SaveProgressDialog


class SaveDataAgent(QObject):
    def __init__(self, parent: Optional[QWidget]):
        super().__init__(parent)
        self.window = parent
        self.meas_times: List[float] = []
        self.meas_values: List[float] = []
        self.worker: Optional[SaveDataWorker] = None
        self.threadpool = QThreadPool()
        self.progress_dlg: Optional[SaveProgressDialog] = None

    kill_thread = Signal()

    def save(
        self,
        meas_times: List[float],
        meas_values: List[float],
        *,
        auto_save_file: bool = True,
        gui: bool = True,
        start_time: Optional[datetime] = None,
    ) -> None:
        self.meas_times = meas_times.copy()
        self.meas_values = meas_values.copy()
        if auto_save_file or not gui:
            if start_time is None:
                file_time = datetime.now()
            else:
                file_time = start_time
            basefilename = (
                f"{file_time.year}-{file_time.month:02d}-{file_time.day:02d}-"
                f"{file_time.hour:02d}:{file_time.minute:02d}:"
                f"{file_time.second:02d}.tsv"
            )
            save_dir = app_config.save_dir()
            self.write_results_file(save_dir / basefilename, gui=gui)
        else:
            dialog = QFileDialog(self.window)
            dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
            dialog.setFileMode(QFileDialog.FileMode.AnyFile)
            dialog.setDefaultSuffix("tsv")
            dialog.setDirectory(str(app_config.save_dir()))
            dialog.setNameFilter("*.tsv *.csv")
            if dialog.exec():
                filenames = dialog.selectedFiles()
                self.write_results_file(Path(filenames[0]).resolve(), gui=True)
            else:
                logging.info("Saving canceled")

    def write_results_file(self, output_path: Path, *, gui: bool = True) -> None:
        logging.info(f"Saving to {output_path}")
        # Create Worker thread to save the data
        worker = SaveDataWorker(self.meas_times.copy(), self.meas_values.copy(), output_path)
        worker.signals.finished.connect(self.thread_complete)
        self.kill_thread.connect(worker.kill)
        if gui:
            self.progress_dlg = SaveProgressDialog()
            worker.signals.progress.connect(self.progress_dlg.update_progress)
            self.threadpool.start(worker)
            if self.progress_dlg.exec() == QDialog.DialogCode.Rejected:
                self.kill_thread.emit()

    def thread_complete(self) -> None:
        if self.progress_dlg is not None:
            self.progress_dlg.done(QDialog.DialogCode.Accepted)
