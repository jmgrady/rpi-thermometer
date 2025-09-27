# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'saveprogressdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QProgressBar, QSizePolicy, QWidget)

class Ui_SaveProgressDialog(object):
    def setupUi(self, SaveProgressDialog: QDialog) -> None:
        if not SaveProgressDialog.objectName():
            SaveProgressDialog.setObjectName(u"SaveProgressDialog")
        SaveProgressDialog.resize(410, 137)
        self.buttonBox = QDialogButtonBox(SaveProgressDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 90, 381, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel)
        self.saving_to_label = QLabel(SaveProgressDialog)
        self.saving_to_label.setObjectName(u"saving_to_label")
        self.saving_to_label.setGeometry(QRect(20, 20, 66, 18))
        self.saving_to_field = QLabel(SaveProgressDialog)
        self.saving_to_field.setObjectName(u"saving_to_field")
        self.saving_to_field.setGeometry(QRect(90, 20, 511, 18))
        self.save_progress = QProgressBar(SaveProgressDialog)
        self.save_progress.setObjectName(u"save_progress")
        self.save_progress.setGeometry(QRect(40, 50, 341, 23))
        self.save_progress.setValue(24)

        self.retranslateUi(SaveProgressDialog)
        self.buttonBox.accepted.connect(SaveProgressDialog.accept)
        self.buttonBox.rejected.connect(SaveProgressDialog.reject)

        QMetaObject.connectSlotsByName(SaveProgressDialog)
    # setupUi

    def retranslateUi(self, SaveProgressDialog: QDialog) -> None:
        SaveProgressDialog.setWindowTitle(QCoreApplication.translate("SaveProgressDialog", u"File save Progress", None))
        self.saving_to_label.setText(QCoreApplication.translate("SaveProgressDialog", u"Saving to", None))
        self.saving_to_field.setText(QCoreApplication.translate("SaveProgressDialog", u"...", None))
    # retranslateUi

