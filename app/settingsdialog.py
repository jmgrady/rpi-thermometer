import logging
from pathlib import Path
from typing import Optional

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog, QFileDialog, QWidget
from appconfig import AppConfig, Sensors, Units
from ui.ui_settingsdialog import Ui_SettingsDialog


class SettingsDialog(QDialog):
    def __init__(self, config: AppConfig, parent: Optional[QWidget] = None):
        super(SettingsDialog, self).__init__(parent)
        self.config = config
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)

    def show(self) -> None:
        self.load_dlg_from_config()
        self.ui.save_dir_dialog.clicked.connect(self.get_save_dir)
        if self.exec() == QDialog.DialogCode.Accepted:
            self.load_config_from_dlg()

    @Slot()
    def get_save_dir(self) -> None:
        start_dir = self.ui.save_directory.text()
        file_dlg = QFileDialog(self)
        file_dlg.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        file_dlg.setFileMode(QFileDialog.FileMode.Directory)
        file_dlg.setDirectory(start_dir)
        if file_dlg.exec():
            self.ui.save_directory.setText(file_dlg.selectedFiles()[0])

    def load_dlg_from_config(self) -> None:
        self.ui.sample_period.setValue(self.config.sample_period())
        units = self.config.units()
        if units == Units.DEG_C:
            self.ui.units_deg_c.setChecked(True)
            self.ui.units_deg_f.setChecked(False)
        else:
            self.ui.units_deg_c.setChecked(False)
            self.ui.units_deg_f.setChecked(True)
        self.ui.save_directory.setText(str(self.config.save_dir()))
        sensor = self.config.sensor_type()
        if sensor == Sensors.SPI:
            self.ui.sensor_spi.setChecked(True)
            self.ui.sensor_1_wire.setChecked(False)
            self.ui.sensor_simulated.setChecked(False)
        elif sensor == Sensors.ONE_WIRE:
            self.ui.sensor_spi.setChecked(False)
            self.ui.sensor_1_wire.setChecked(True)
            self.ui.sensor_simulated.setChecked(False)
        else:
            self.ui.sensor_spi.setChecked(False)
            self.ui.sensor_1_wire.setChecked(False)
            self.ui.sensor_simulated.setChecked(True)
            if sensor != Sensors.SIM:
                logging.warning(f"Unrecognized sensor type: {sensor}")

    def load_config_from_dlg(self) -> None:
        self.config.set_sample_period(self.ui.sample_period.value())
        if self.ui.units_deg_c.isChecked():
            self.config.set_units(Units.DEG_C)
        else:
            self.config.set_units(Units.DEG_F)
        save_dir = Path(self.ui.save_directory.text()).resolve()
        if not save_dir.exists():
            save_dir.mkdir(parents=True)
            logging.info(f"Creating save directory: {save_dir}.")
        elif not save_dir.is_dir():
            logging.error(f"{save_dir} is not a directory.")
        else:
            self.config.set_save_dir(save_dir)
        if self.ui.sensor_spi.isChecked():
            self.config.set_sensor_type(Sensors.SPI)
        elif self.ui.sensor_1_wire.isChecked():
            self.config.set_sensor_type(Sensors.ONE_WIRE)
        else:
            self.config.set_sensor_type(Sensors.SIM)
