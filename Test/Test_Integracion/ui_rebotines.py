# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rebotines.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSlider, QStatusBar, QToolBar,
    QWidget)
import recursos_rebotines

class Ui_MainWindow_Rebotines(object):
        
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.velocidad = 750
        self.actionPlay_Resume = QAction(MainWindow)
        self.actionPlay_Resume.setObjectName(u"actionPlay_Resume")
        icon = QIcon()
        icon.addFile(u":/botones/boton-doble.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPlay_Resume.setIcon(icon)
        self.actionStop = QAction(MainWindow)
        self.actionStop.setObjectName(u"actionStop")
        icon1 = QIcon()
        icon1.addFile(u":/botones/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionStop.setIcon(icon1)
        self.actionAdvance_velocity = QAction(MainWindow)
        self.actionAdvance_velocity.setObjectName(u"actionAdvance_velocity")
        icon2 = QIcon()
        icon2.addFile(u":/botones/fast-forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAdvance_velocity.setIcon(icon2)
        self.actionRewind_velocity = QAction(MainWindow)
        self.actionRewind_velocity.setObjectName(u"actionRewind_velocity")
        icon3 = QIcon()
        icon3.addFile(u":/botones/rewind.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRewind_velocity.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(10, 500, 781, 16))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setStyleSheet("color:yellow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuAcciones = QMenu(self.menubar)
        self.menuAcciones.setObjectName(u"menuAcciones")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuAcciones.menuAction())
        self.menuAcciones.addAction(self.actionPlay_Resume)
        self.menuAcciones.addAction(self.actionStop)
        self.menuAcciones.addAction(self.actionAdvance_velocity)
        self.menuAcciones.addAction(self.actionRewind_velocity)
        self.toolBar.addAction(self.actionStop)
        self.toolBar.addAction(self.actionRewind_velocity)
        self.toolBar.addAction(self.actionPlay_Resume)
        self.toolBar.addAction(self.actionAdvance_velocity)

        
        

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionPlay_Resume.setText(QCoreApplication.translate("MainWindow", u"Play/Resume", None))
#if QT_CONFIG(shortcut)
        self.actionPlay_Resume.setShortcut(QCoreApplication.translate("MainWindow", u"Toggle Media Play/Pause", None))
#endif // QT_CONFIG(shortcut)
        self.actionStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
#if QT_CONFIG(shortcut)
        self.actionStop.setShortcut(QCoreApplication.translate("MainWindow", u"Media Stop", None))
#endif // QT_CONFIG(shortcut)
        self.actionAdvance_velocity.setText(QCoreApplication.translate("MainWindow", u"Advance (velocity)", None))
#if QT_CONFIG(shortcut)
        self.actionAdvance_velocity.setShortcut(QCoreApplication.translate("MainWindow", u"Media Next", None))
#endif // QT_CONFIG(shortcut)
        self.actionRewind_velocity.setText(QCoreApplication.translate("MainWindow", u"Rewind (velocity)", None))
#if QT_CONFIG(shortcut)
        self.actionRewind_velocity.setShortcut(QCoreApplication.translate("MainWindow", u"Media Previous", None))
#endif // QT_CONFIG(shortcut)
        self.menuAcciones.setTitle(QCoreApplication.translate("MainWindow", u"Actions", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

