from typing import Optional

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog, QWidget
from ui.ui_saveprogressdialog import Ui_SaveProgressDialog


class SaveProgressDialog(QDialog):
    def __init__(
        self,
        parent: Optional[QWidget] = None,
    ):
        super(SaveProgressDialog, self).__init__(parent)
        self.ui = Ui_SaveProgressDialog()
        self.ui.setupUi(self)

    def show(self) -> None:
        self.ui.save_progress.setValue(0)
        self.exec()

    @Slot(float)
    def update_progress(self, progress: float) -> None:
        self.ui.save_progress.setValue(round(progress))

    def copy_finished(self) -> None:
        self.done(QDialog.DialogCode.Accepted)
