from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QPen
from datatypes import GraphConfig
import pyqtgraph as pg

graph_config = GraphConfig(
    [(255, 0, 0), (0, 0, 255)],
    {"raw": Qt.PenStyle.SolidLine, "avg": Qt.PenStyle.DotLine},
    (0, 127, 0),
)


def get_pen(series: str, channel: int) -> QPen:
    if series == "mark":
        return QPen(Qt.PenStyle.NoPen)
    else:
        return QPen(pg.mkPen(color=graph_config.colors[channel], style=graph_config.style[series]))


def get_brush(series: str) -> Optional[QBrush]:
    if series == "mark":
        return QBrush(pg.mkBrush(color=graph_config.mark))
    else:
        return None
