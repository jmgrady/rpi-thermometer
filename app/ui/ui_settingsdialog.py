# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
    Qt,
    QTime,
    QUrl,
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
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QDoubleSpinBox,
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


class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog: QDialog) -> None:
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(640, 357)
        self.buttonBox = QDialogButtonBox(SettingsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 310, 621, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label_settings = QLabel(SettingsDialog)
        self.label_settings.setObjectName(u"label_settings")
        self.label_settings.setGeometry(QRect(30, 20, 91, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_settings.setFont(font)
        self.tabs_settings = QTabWidget(SettingsDialog)
        self.tabs_settings.setObjectName(u"tabs_settings")
        self.tabs_settings.setGeometry(QRect(30, 60, 601, 241))
        font1 = QFont()
        font1.setPointSize(14)
        self.tabs_settings.setFont(font1)
        self.uiSettingsTab = QWidget()
        self.uiSettingsTab.setObjectName(u"uiSettingsTab")
        self.label_units = QLabel(self.uiSettingsTab)
        self.label_units.setObjectName(u"label_units")
        self.label_units.setGeometry(QRect(30, 20, 91, 18))
        self.units_deg_c = QRadioButton(self.uiSettingsTab)
        self.units_deg_c.setObjectName(u"units_deg_c")
        self.units_deg_c.setGeometry(QRect(190, 20, 61, 23))
        self.units_deg_f = QRadioButton(self.uiSettingsTab)
        self.units_deg_f.setObjectName(u"units_deg_f")
        self.units_deg_f.setGeometry(QRect(260, 20, 51, 23))
        self.units_deg_f.setChecked(True)
        self.label_period = QLabel(self.uiSettingsTab)
        self.label_period.setObjectName(u"label_period")
        self.label_period.setGeometry(QRect(30, 50, 151, 18))
        self.label_period_units = QLabel(self.uiSettingsTab)
        self.label_period_units.setObjectName(u"label_period_units")
        self.label_period_units.setGeometry(QRect(260, 50, 81, 18))
        self.save_dir_label = QLabel(self.uiSettingsTab)
        self.save_dir_label.setObjectName(u"save_dir_label")
        self.save_dir_label.setGeometry(QRect(30, 144, 141, 18))
        self.save_directory = QLineEdit(self.uiSettingsTab)
        self.save_directory.setObjectName(u"save_directory")
        self.save_directory.setGeometry(QRect(170, 140, 381, 26))
        self.save_dir_dialog = QToolButton(self.uiSettingsTab)
        self.save_dir_dialog.setObjectName(u"save_dir_dialog")
        self.save_dir_dialog.setGeometry(QRect(550, 140, 26, 25))
        icon = QIcon()
        icon.addFile(u":/resources/icons/folder-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_dir_dialog.setIcon(icon)
        self.save_dir_dialog.setIconSize(QSize(24, 24))
        self.sample_period = QDoubleSpinBox(self.uiSettingsTab)
        self.sample_period.setObjectName(u"sample_period")
        self.sample_period.setGeometry(QRect(190, 46, 65, 27))
        self.sample_period.setDecimals(1)
        self.sample_period.setValue(10.000000000000000)
        self.label_running_avg = QLabel(self.uiSettingsTab)
        self.label_running_avg.setObjectName(u"label_running_avg")
        self.label_running_avg.setGeometry(QRect(30, 80, 151, 31))
        self.running_avg_time = QDoubleSpinBox(self.uiSettingsTab)
        self.running_avg_time.setObjectName(u"running_avg_time")
        self.running_avg_time.setGeometry(QRect(190, 80, 65, 27))
        self.running_avg_time.setDecimals(1)
        self.running_avg_time.setValue(10.000000000000000)
        self.running_avg_units = QComboBox(self.uiSettingsTab)
        self.running_avg_units.addItem("")
        self.running_avg_units.addItem("")
        self.running_avg_units.setObjectName(u"running_avg_units")
        self.running_avg_units.setGeometry(QRect(260, 80, 101, 26))
        self.running_avg_units.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.tabs_settings.addTab(self.uiSettingsTab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 70, 131, 18))
        self.sensor_spi = QRadioButton(self.tab_2)
        self.sensor_spi.setObjectName(u"sensor_spi")
        self.sensor_spi.setGeometry(QRect(60, 90, 110, 23))
        self.sensor_spi.setChecked(False)
        self.sensor_simulated = QRadioButton(self.tab_2)
        self.sensor_simulated.setObjectName(u"sensor_simulated")
        self.sensor_simulated.setGeometry(QRect(60, 120, 110, 23))
        self.sensor_simulated.setChecked(True)
        self.num_sensors = QSpinBox(self.tab_2)
        self.num_sensors.setObjectName(u"num_sensors")
        self.num_sensors.setGeometry(QRect(200, 20, 44, 27))
        self.num_sensors.setMinimum(1)
        self.num_sensors.setMaximum(2)
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 30, 181, 18))
        self.simulated_sensor_type = QComboBox(self.tab_2)
        self.simulated_sensor_type.setObjectName(u"simulated_sensor_type")
        self.simulated_sensor_type.setGeometry(QRect(190, 120, 201, 26))
        self.sim_wave_freq = QDoubleSpinBox(self.tab_2)
        self.sim_wave_freq.setObjectName(u"sim_wave_freq")
        self.sim_wave_freq.setGeometry(QRect(200, 150, 65, 27))
        self.freq_label = QLabel(self.tab_2)
        self.freq_label.setObjectName(u"freq_label")
        self.freq_label.setGeometry(QRect(80, 150, 111, 27))
        self.freq_units_lbl = QLabel(self.tab_2)
        self.freq_units_lbl.setObjectName(u"freq_units_lbl")
        self.freq_units_lbl.setGeometry(QRect(270, 150, 31, 27))
        self.tabs_settings.addTab(self.tab_2, "")

        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)

        self.tabs_settings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog: QDialog) -> None:
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.label_settings.setText(QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.label_units.setText(QCoreApplication.translate("SettingsDialog", u"Units:", None))
        self.units_deg_c.setText(QCoreApplication.translate("SettingsDialog", u"\u00b0C", None))
        self.units_deg_f.setText(QCoreApplication.translate("SettingsDialog", u"\u00b0F", None))
        self.label_period.setText(QCoreApplication.translate("SettingsDialog", u"Sample Period:", None))
        self.label_period_units.setText(QCoreApplication.translate("SettingsDialog", u"seconds", None))
        self.save_dir_label.setText(QCoreApplication.translate("SettingsDialog", u"Save Directory:", None))
        self.save_dir_dialog.setText("")
        self.label_running_avg.setText(QCoreApplication.translate("SettingsDialog", u"Running Average", None))
        self.running_avg_units.setItemText(0, QCoreApplication.translate("SettingsDialog", u"seconds", None))
        self.running_avg_units.setItemText(1, QCoreApplication.translate("SettingsDialog", u"minutes", None))

        self.tabs_settings.setTabText(self.tabs_settings.indexOf(self.uiSettingsTab), QCoreApplication.translate("SettingsDialog", u"User Interface", None))
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"Sensor Type:", None))
        self.sensor_spi.setText(QCoreApplication.translate("SettingsDialog", u"SPI", None))
        self.sensor_simulated.setText(QCoreApplication.translate("SettingsDialog", u"Simulated", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"Number of Sensors:", None))
        self.freq_label.setText(QCoreApplication.translate("SettingsDialog", u"Frequency:", None))
        self.freq_units_lbl.setText(QCoreApplication.translate("SettingsDialog", u"Hz", None))
        self.tabs_settings.setTabText(self.tabs_settings.indexOf(self.tab_2), QCoreApplication.translate("SettingsDialog", u"Devices", None))
    # retranslateUi

