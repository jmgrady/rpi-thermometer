# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractButton,
    QApplication,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QLineEdit,
    QRadioButton,
    QSizePolicy,
    QSpinBox,
    QTabWidget,
    QToolButton,
    QWidget,
)
import ui.resources_rc


class Ui_SettingsDialog(QDialog):
    def setupUi(self, SettingsDialog: QDialog) -> None:
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(640, 480)
        self.buttonBox = QDialogButtonBox(SettingsDialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setGeometry(QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok
        )
        self.label_settings = QLabel(SettingsDialog)
        self.label_settings.setObjectName("label_settings")
        self.label_settings.setGeometry(QRect(30, 20, 91, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_settings.setFont(font)
        self.tabs_settings = QTabWidget(SettingsDialog)
        self.tabs_settings.setObjectName("tabs_settings")
        self.tabs_settings.setGeometry(QRect(30, 60, 601, 361))
        font1 = QFont()
        font1.setPointSize(14)
        self.tabs_settings.setFont(font1)
        self.uiSettingsTab = QWidget()
        self.uiSettingsTab.setObjectName("uiSettingsTab")
        self.label_units = QLabel(self.uiSettingsTab)
        self.label_units.setObjectName("label_units")
        self.label_units.setGeometry(QRect(30, 40, 91, 18))
        self.units_deg_c = QRadioButton(self.uiSettingsTab)
        self.units_deg_c.setObjectName("units_deg_c")
        self.units_deg_c.setGeometry(QRect(190, 40, 61, 23))
        self.units_deg_f = QRadioButton(self.uiSettingsTab)
        self.units_deg_f.setObjectName("units_deg_f")
        self.units_deg_f.setGeometry(QRect(260, 40, 51, 23))
        self.label_period = QLabel(self.uiSettingsTab)
        self.label_period.setObjectName("label_period")
        self.label_period.setGeometry(QRect(30, 90, 151, 18))
        self.sample_period = QSpinBox(self.uiSettingsTab)
        self.sample_period.setObjectName("sample_period")
        self.sample_period.setGeometry(QRect(180, 86, 61, 27))
        self.label_period_units = QLabel(self.uiSettingsTab)
        self.label_period_units.setObjectName("label_period_units")
        self.label_period_units.setGeometry(QRect(260, 90, 81, 18))
        self.save_dir_label = QLabel(self.uiSettingsTab)
        self.save_dir_label.setObjectName("save_dir_label")
        self.save_dir_label.setGeometry(QRect(30, 144, 141, 18))
        self.save_directory = QLineEdit(self.uiSettingsTab)
        self.save_directory.setObjectName("save_directory")
        self.save_directory.setGeometry(QRect(170, 140, 381, 26))
        self.save_dir_dialog = QToolButton(self.uiSettingsTab)
        self.save_dir_dialog.setObjectName("save_dir_dialog")
        self.save_dir_dialog.setGeometry(QRect(550, 140, 26, 25))
        icon = QIcon()
        icon.addFile(
            ":/resources/icons/folder-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.save_dir_dialog.setIcon(icon)
        self.save_dir_dialog.setIconSize(QSize(24, 24))
        self.tabs_settings.addTab(self.uiSettingsTab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(20, 30, 131, 18))
        self.sensor_spi = QRadioButton(self.tab_2)
        self.sensor_spi.setObjectName("sensor_spi")
        self.sensor_spi.setGeometry(QRect(60, 60, 110, 23))
        self.sensor_spi.setChecked(True)
        self.sensor_1_wire = QRadioButton(self.tab_2)
        self.sensor_1_wire.setObjectName("sensor_1_wire")
        self.sensor_1_wire.setGeometry(QRect(60, 100, 110, 23))
        self.sensor_simulated = QRadioButton(self.tab_2)
        self.sensor_simulated.setObjectName("sensor_simulated")
        self.sensor_simulated.setGeometry(QRect(60, 140, 110, 23))
        self.tabs_settings.addTab(self.tab_2, "")

        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)

        self.tabs_settings.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(SettingsDialog)

    # setupUi

    def retranslateUi(self, SettingsDialog: QDialog) -> None:
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", "Dialog", None))
        self.label_settings.setText(QCoreApplication.translate("SettingsDialog", "Settings", None))
        self.label_units.setText(QCoreApplication.translate("SettingsDialog", "Units:", None))
        self.units_deg_c.setText(QCoreApplication.translate("SettingsDialog", "\u00b0C", None))
        self.units_deg_f.setText(QCoreApplication.translate("SettingsDialog", "\u00b0F", None))
        self.label_period.setText(
            QCoreApplication.translate("SettingsDialog", "Sample Period:", None)
        )
        self.label_period_units.setText(
            QCoreApplication.translate("SettingsDialog", "seconds", None)
        )
        self.save_dir_label.setText(
            QCoreApplication.translate("SettingsDialog", "Save Directory:", None)
        )
        self.save_dir_dialog.setText("")
        self.tabs_settings.setTabText(
            self.tabs_settings.indexOf(self.uiSettingsTab),
            QCoreApplication.translate("SettingsDialog", "User Interface", None),
        )
        self.label.setText(QCoreApplication.translate("SettingsDialog", "Sensor Type:", None))
        self.sensor_spi.setText(QCoreApplication.translate("SettingsDialog", "SPI", None))
        self.sensor_1_wire.setText(QCoreApplication.translate("SettingsDialog", "1-Wire", None))
        self.sensor_simulated.setText(
            QCoreApplication.translate("SettingsDialog", "Simulated", None)
        )
        self.tabs_settings.setTabText(
            self.tabs_settings.indexOf(self.tab_2),
            QCoreApplication.translate("SettingsDialog", "Devices", None),
        )

    # retranslateUi
