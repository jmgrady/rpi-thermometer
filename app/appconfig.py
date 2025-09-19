from enum import Enum, unique
import os
from pathlib import Path

from PySide6.QtCore import QSettings


@unique
class Units(Enum):
    DEG_C = "C"
    DEG_F = "F"


@unique
class Sensors(Enum):
    SPI = "SPI"
    ONE_WIRE = "1-wire"
    SIM = "Simulated"


@unique
class ConfigItem(Enum):
    UNITS = "units"
    PERIOD = "period"
    SAVE_DIR = "save_dir"
    SENSOR_TYPE = "sensor_type"


class AppConfig(QSettings):
    def __init__(self, scope: str, app_name: str):
        super(AppConfig, self).__init__(scope, app_name)

    def sample_period(self) -> float:
        period = self.value(ConfigItem.PERIOD.value, 15.0)
        return period  # type: ignore[return-value]

    def set_sample_period(self, period: float) -> None:
        self.setValue(ConfigItem.PERIOD.value, period)

    def units(self) -> Units:
        unit_str = self.value(ConfigItem.UNITS.value, Units.DEG_F.value)
        if unit_str == "C":
            return Units.DEG_C
        else:
            return Units.DEG_F

    def set_units(self, units: Units) -> None:
        self.setValue(ConfigItem.UNITS.value, units.value)

    def save_dir(self) -> Path:
        home_dir = os.getenv("HOME")
        if home_dir is not None:
            default_dir = Path(home_dir).resolve() / "rpi-thermometer"
        else:
            default_dir = Path("/opt/rpi/data")
        save_dir = self.value(ConfigItem.SAVE_DIR.value, str(default_dir))
        return Path(save_dir).resolve()  # type: ignore[arg-type]

    def set_save_dir(self, save_path: Path) -> None:
        self.setValue(ConfigItem.SAVE_DIR.value, str(save_path))

    def sensor_type(self) -> Sensors:
        sensor_str = self.value(ConfigItem.SENSOR_TYPE.value, Sensors.SIM.value, str)
        if sensor_str == Sensors.SIM.value:
            return Sensors.SIM
        elif sensor_str == Sensors.ONE_WIRE.value:
            return Sensors.ONE_WIRE
        else:
            return Sensors.SPI

    def set_sensor_type(self, sensor: Sensors) -> None:
        self.setValue(ConfigItem.SENSOR_TYPE.value, sensor.value)
