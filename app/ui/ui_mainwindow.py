# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
        MainWindow.resize(800, 480)
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
        self.formLayoutWidget.setGeometry(QRect(20, 10, 501, 115))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.tempLabel = QLabel(self.formLayoutWidget)
        self.tempLabel.setObjectName(u"tempLabel")
        self.tempLabel.setMinimumSize(QSize(0, 78))
        font1 = QFont()
        font1.setPointSize(18)
        self.tempLabel.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.tempLabel)

        self.tempValue = QLabel(self.formLayoutWidget)
        self.tempValue.setObjectName(u"tempValue")
        font2 = QFont()
        font2.setPointSize(36)
        self.tempValue.setFont(font2)
        self.tempValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.tempValue)

        self.timeLabel = QLabel(self.formLayoutWidget)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.timeLabel)

        self.elapsedTimeValue = QLabel(self.formLayoutWidget)
        self.elapsedTimeValue.setObjectName(u"elapsedTimeValue")
        self.elapsedTimeValue.setFont(font1)
        self.elapsedTimeValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.elapsedTimeValue)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(570, 10, 48, 48))
        font3 = QFont()
        font3.setPointSize(20)
        self.startButton.setFont(font3)
        icon1 = QIcon()
        icon1.addFile(u":/resources/icons/media-play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.startButton.setIcon(icon1)
        self.startButton.setIconSize(QSize(48, 48))
        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setEnabled(False)
        self.stopButton.setGeometry(QRect(650, 10, 48, 48))
        self.stopButton.setFont(font3)
        icon2 = QIcon()
        icon2.addFile(u":/resources/icons/media-stop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stopButton.setIcon(icon2)
        self.stopButton.setIconSize(QSize(48, 48))
        self.graphWindow = PlotWidget(self.centralwidget)
        self.graphWindow.setObjectName(u"graphWindow")
        self.graphWindow.setGeometry(QRect(20, 150, 701, 271))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 34))
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
        self.startButton.setText("")
        self.stopButton.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

