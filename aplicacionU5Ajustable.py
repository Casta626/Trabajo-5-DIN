# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aplicacionU5Ajustable.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QColumnView, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)
import recursos

class Ui_MainWindowAjustable(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(499, 537)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelGrafica = QLabel(self.tab)
        self.labelGrafica.setObjectName(u"labelGrafica")
        self.labelGrafica.setMaximumSize(QSize(180, 180))
        self.labelGrafica.setPixmap(QPixmap(u":/CastaPC/81XHNWut5WL._AC_SL1500_.jpg"))
        self.labelGrafica.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.labelGrafica)

        self.checkBoxGrafica = QCheckBox(self.tab)
        self.checkBoxGrafica.setObjectName(u"checkBoxGrafica")

        self.verticalLayout_4.addWidget(self.checkBoxGrafica)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(180, 180))
        self.label_2.setPixmap(QPixmap(u":/CastaPC/fuente-alimentacion-atx-850w-gigabyte-80--gold-modular--gp-p850gm-main.jpg"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label_2)

        self.checkBoxFuenteAlimentacion = QCheckBox(self.tab)
        self.checkBoxFuenteAlimentacion.setObjectName(u"checkBoxFuenteAlimentacion")

        self.verticalLayout_2.addWidget(self.checkBoxFuenteAlimentacion)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelProcesador = QLabel(self.tab)
        self.labelProcesador.setObjectName(u"labelProcesador")
        self.labelProcesador.setMaximumSize(QSize(180, 180))
        self.labelProcesador.setPixmap(QPixmap(u":/CastaPC/amd-ryzen-5-3600-36ghz.jpg"))
        self.labelProcesador.setScaledContents(True)

        self.verticalLayout.addWidget(self.labelProcesador)

        self.checkBoxProcesador = QCheckBox(self.tab)
        self.checkBoxProcesador.setObjectName(u"checkBoxProcesador")

        self.verticalLayout.addWidget(self.checkBoxProcesador)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelCaja = QLabel(self.tab)
        self.labelCaja.setObjectName(u"labelCaja")
        self.labelCaja.setMaximumSize(QSize(180, 180))
        self.labelCaja.setPixmap(QPixmap(u":/CastaPC/wipoid-pc-gaming-sniper.jpg"))
        self.labelCaja.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.labelCaja)

        self.checkBox_Caja = QCheckBox(self.tab)
        self.checkBox_Caja.setObjectName(u"checkBox_Caja")

        self.verticalLayout_3.addWidget(self.checkBox_Caja)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.columnView = QColumnView(self.tab_3)
        self.columnView.setObjectName(u"columnView")

        self.horizontalLayout_3.addWidget(self.columnView)

        self.tabWidget.addTab(self.tab_3, "")

        self.horizontalLayout_4.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 499, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelGrafica.setText("")
        self.checkBoxGrafica.setText(QCoreApplication.translate("MainWindow", u"RTX 3090 Titan 24GB", None))
        self.label_2.setText("")
        self.checkBoxFuenteAlimentacion.setText(QCoreApplication.translate("MainWindow", u"Fuente de Alimentaci\u00f3n 850 w", None))
        self.labelProcesador.setText("")
        self.checkBoxProcesador.setText(QCoreApplication.translate("MainWindow", u"AMD Ryzen 5 3600", None))
        self.labelCaja.setText("")
        self.checkBox_Caja.setText(QCoreApplication.translate("MainWindow", u"Caja Extended ATX ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Compra de PCs", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Reparaci\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Base de Datos", None))
    # retranslateUi

