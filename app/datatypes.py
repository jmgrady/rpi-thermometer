from dataclasses import dataclass
from typing import Dict, List, Tuple

from PySide6.QtCore import Qt


@dataclass
class Measurements:
    times: List[float]
    # values are treated as a 2D array with a column for each measurement
    # channel
    values: List[float]


@dataclass
class GraphConfig:
    colors: List[Tuple[int, int, int]]
    style: Dict[str, Qt.PenStyle]
    mark: Tuple[int, int, int]  # Color for marking graph
