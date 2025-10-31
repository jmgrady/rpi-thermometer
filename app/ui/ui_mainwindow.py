# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
    QAction,
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
    QApplication,
    QFormLayout,
    QLabel,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QWidget,
)
from pyqtgraph import PlotWidget
import ui.resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QMainWindow) -> None:
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 430)
        font = QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/resources/icons/thermometer-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(True)
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 10, 501, 81))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.tempLabel = QLabel(self.formLayoutWidget)
        self.tempLabel.setObjectName(u"tempLabel")
        self.tempLabel.setMinimumSize(QSize(0, 78))
        font1 = QFont()
        font1.setPointSize(12)
        self.tempLabel.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.tempLabel)

        self.tempValue = QLabel(self.formLayoutWidget)
        self.tempValue.setObjectName(u"tempValue")
        font2 = QFont()
        font2.setPointSize(24)
        self.tempValue.setFont(font2)
        self.tempValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.tempValue)

        self.timeLabel = QLabel(self.formLayoutWidget)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.timeLabel)

        self.elapsedTimeValue = QLabel(self.formLayoutWidget)
        self.elapsedTimeValue.setObjectName(u"elapsedTimeValue")
        self.elapsedTimeValue.setFont(font1)
        self.elapsedTimeValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.elapsedTimeValue)

        self.graphWindow = PlotWidget(self.centralwidget)
        self.graphWindow.setObjectName(u"graphWindow")
        self.graphWindow.setGeometry(QRect(20, 109, 761, 271))
        self.startStopButton = QPushButton(self.centralwidget)
        self.startStopButton.setObjectName(u"startStopButton")
        self.startStopButton.setGeometry(QRect(530, 10, 71, 61))
        icon1 = QIcon()
        icon1.addFile(u":/resources/icons/media-record.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.startStopButton.setIcon(icon1)
        self.startStopButton.setIconSize(QSize(48, 48))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menubar.setFont(font1)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setFont(font1)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow: QMainWindow) -> None:
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Thermometer", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings...", None))
#if QT_CONFIG(shortcut)
        self.actionSettings.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+,", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As ...", None))
        self.tempLabel.setText(QCoreApplication.translate("MainWindow", u"Temperature:", None))
        self.tempValue.setText(QCoreApplication.translate("MainWindow", u"-?-", None))
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"Elapsed Time:", None))
        self.elapsedTimeValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.startStopButton.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

