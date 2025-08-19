# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        font = QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(True)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(60, 30, 531, 133))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tempValue = QLabel(self.gridLayoutWidget)
        self.tempValue.setObjectName(u"tempValue")
        font1 = QFont()
        font1.setPointSize(36)
        self.tempValue.setFont(font1)
        self.tempValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.tempValue, 0, 1, 1, 1)

        self.timeLabel = QLabel(self.gridLayoutWidget)
        self.timeLabel.setObjectName(u"timeLabel")
        font2 = QFont()
        font2.setPointSize(24)
        self.timeLabel.setFont(font2)

        self.gridLayout.addWidget(self.timeLabel, 1, 0, 1, 1)

        self.tempLabel = QLabel(self.gridLayoutWidget)
        self.tempLabel.setObjectName(u"tempLabel")
        self.tempLabel.setMinimumSize(QSize(0, 78))
        self.tempLabel.setFont(font2)

        self.gridLayout.addWidget(self.tempLabel, 0, 0, 1, 1)

        self.elapsedTimeValue = QLabel(self.gridLayoutWidget)
        self.elapsedTimeValue.setObjectName(u"elapsedTimeValue")
        self.elapsedTimeValue.setFont(font2)
        self.elapsedTimeValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.elapsedTimeValue, 1, 1, 1, 1)

        self.loggingEnabled = QCheckBox(self.centralwidget)
        self.loggingEnabled.setObjectName(u"loggingEnabled")
        self.loggingEnabled.setGeometry(QRect(70, 190, 141, 23))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 230, 431, 26))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 34))
        font3 = QFont()
        font3.setPointSize(18)
        self.menubar.setFont(font3)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings...", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.tempValue.setText(QCoreApplication.translate("MainWindow", u"-?-", None))
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"Elapsed Time:", None))
        self.tempLabel.setText(QCoreApplication.translate("MainWindow", u"Temperature:", None))
        self.elapsedTimeValue.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.loggingEnabled.setText(QCoreApplication.translate("MainWindow", u"Log to file", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

