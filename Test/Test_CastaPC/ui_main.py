# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aplicacionU5Ajustable.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListView, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableView, QVBoxLayout,
    QWidget)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
import recursos
from rebotines import MainWindowRebotines

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(562, 567)
        self.actionInsertar = QAction(MainWindow)
        self.actionInsertar.setObjectName(u"actionInsertar")
        icon = QIcon()
        icon.addFile(u":/CastaPC/database--plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionInsertar.setIcon(icon)
        self.actionModificar = QAction(MainWindow)
        self.actionModificar.setObjectName(u"actionModificar")
        icon1 = QIcon()
        icon1.addFile(u":/CastaPC/database--arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionModificar.setIcon(icon1)
        self.actionEliminar = QAction(MainWindow)
        self.actionEliminar.setObjectName(u"actionEliminar")
        icon2 = QIcon()
        icon2.addFile(u":/CastaPC/database--minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEliminar.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")

        self.tabComponente = QWidget()
        self.tabComponente.setObjectName(u"tabComponente")
        self.verticalLayout = QVBoxLayout(self.tabComponente)


        self.tabCompras = QWidget()
        self.tabCompras.setObjectName(u"tabCompras")
        self.verticalLayout = QVBoxLayout(self.tabCompras)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vLayoutCompras = QVBoxLayout()
        self.vLayoutCompras.setObjectName(u"vLayoutCompras")
        self.hLayoutG_FA = QHBoxLayout()
        self.hLayoutG_FA.setObjectName(u"hLayoutG_FA")
        self.vLayoutGrafica = QVBoxLayout()
        self.vLayoutGrafica.setObjectName(u"vLayoutGrafica")
        self.labelGrafica = QLabel(self.tabCompras)
        self.labelGrafica.setObjectName(u"labelGrafica")
        self.labelGrafica.setMaximumSize(QSize(180, 180))
        self.labelGrafica.setPixmap(QPixmap(u":/CastaPC/81XHNWut5WL._AC_SL1500_.jpg"))
        self.labelGrafica.setScaledContents(True)

        self.vLayoutGrafica.addWidget(self.labelGrafica)

        self.checkBoxGrafica = QCheckBox(self.tabCompras)
        self.checkBoxGrafica.setObjectName(u"checkBoxGrafica")

        self.vLayoutGrafica.addWidget(self.checkBoxGrafica)


        self.hLayoutG_FA.addLayout(self.vLayoutGrafica)

        self.vLayoutFA = QVBoxLayout()
        self.vLayoutFA.setObjectName(u"vLayoutFA")
        self.labelFA = QLabel(self.tabCompras)
        self.labelFA.setObjectName(u"labelFA")
        self.labelFA.setMaximumSize(QSize(180, 180))
        self.labelFA.setPixmap(QPixmap(u":/CastaPC/fuente-alimentacion-atx-850w-gigabyte-80--gold-modular--gp-p850gm-main.jpg"))
        self.labelFA.setScaledContents(True)

        self.vLayoutFA.addWidget(self.labelFA)

        self.checkBoxFA = QCheckBox(self.tabCompras)
        self.checkBoxFA.setObjectName(u"checkBoxFA")

        self.vLayoutFA.addWidget(self.checkBoxFA)


        self.hLayoutG_FA.addLayout(self.vLayoutFA)


        self.vLayoutCompras.addLayout(self.hLayoutG_FA)

        self.hLayoutP_C = QHBoxLayout()
        self.hLayoutP_C.setObjectName(u"hLayoutP_C")
        self.vLayoutProcesaor = QVBoxLayout()
        self.vLayoutProcesaor.setObjectName(u"vLayoutProcesaor")
        self.labelProcesador = QLabel(self.tabCompras)
        self.labelProcesador.setObjectName(u"labelProcesador")
        self.labelProcesador.setMaximumSize(QSize(180, 180))
        self.labelProcesador.setPixmap(QPixmap(u":/CastaPC/amd-ryzen-5-3600-36ghz.jpg"))
        self.labelProcesador.setScaledContents(True)

        self.vLayoutProcesaor.addWidget(self.labelProcesador)

        self.checkBoxProcesador = QCheckBox(self.tabCompras)
        self.checkBoxProcesador.setObjectName(u"checkBoxProcesador")

        self.vLayoutProcesaor.addWidget(self.checkBoxProcesador)


        self.hLayoutP_C.addLayout(self.vLayoutProcesaor)

        self.vLayoutCaja = QVBoxLayout()
        self.vLayoutCaja.setObjectName(u"vLayoutCaja")
        self.labelCaja = QLabel(self.tabCompras)
        self.labelCaja.setObjectName(u"labelCaja")
        self.labelCaja.setMaximumSize(QSize(180, 180))
        self.labelCaja.setPixmap(QPixmap(u":/CastaPC/wipoid-pc-gaming-sniper.jpg"))
        self.labelCaja.setScaledContents(True)

        self.vLayoutCaja.addWidget(self.labelCaja)

        self.checkBoxCaja = QCheckBox(self.tabCompras)
        self.checkBoxCaja.setObjectName(u"checkBoxCaja")

        self.vLayoutCaja.addWidget(self.checkBoxCaja)


        self.hLayoutP_C.addLayout(self.vLayoutCaja)


        self.vLayoutCompras.addLayout(self.hLayoutP_C)


        self.verticalLayout.addLayout(self.vLayoutCompras)

        self.botonAceptarCompras = QPushButton(self.tabCompras)
        self.botonAceptarCompras.setObjectName(u"botonAceptarCompras")
        self.botonAceptarCompras.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.botonAceptarCompras)

        

        icon3 = QIcon()
        icon3.addFile(u":/CastaPC/CompraIcono.png", QSize(), QIcon.Selected, QIcon.Off)
        self.tabWidget.addTab(self.tabCompras, icon3, "")
        self.tabReparacion = QWidget()
        self.tabReparacion.setObjectName(u"tabReparacion")
        self.gridLayout_2 = QGridLayout(self.tabReparacion)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.botonReparacion = QPushButton(self.tabReparacion)
        self.botonReparacion.setObjectName(u"botonReparacion")

        self.botonComponente = QPushButton(self.tabComponente)
        self.botonComponente.setObjectName(u"botonComponente")
        self.botonComponente.setText("Componente")

        self.gridLayout_2.addWidget(self.botonReparacion, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.botonComponente)

        self.labelImagenReparacion = QLabel(self.tabReparacion)
        self.labelImagenReparacion.setObjectName(u"labelImagenReparacion")
        self.labelImagenReparacion.setPixmap(QPixmap(u":/CastaPC/Reparacion.png"))
        self.labelImagenReparacion.setScaledContents(True)

        self.gridLayout_2.addWidget(self.labelImagenReparacion, 0, 0, 1, 1)

        icon4 = QIcon()
        icon4.addFile(u":/CastaPC/ReparacionIcono.png", QSize(), QIcon.Selected, QIcon.Off)
        self.tabWidget.addTab(self.tabReparacion, icon4, "")
        self.tabDB = QWidget()
        self.tabDB.setObjectName(u"tabDB")
        self.verticalLayout_5 = QVBoxLayout(self.tabDB)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox = QGroupBox(self.tabDB)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.labelIDDB = QLabel(self.groupBox)
        self.labelIDDB.setObjectName(u"labelIDDB")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelIDDB)

        self.lineEditIDDB = QLineEdit(self.groupBox)
        self.lineEditIDDB.setObjectName(u"lineEditIDDB")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditIDDB)

        self.labelProductoDB = QLabel(self.groupBox)
        self.labelProductoDB.setObjectName(u"labelProductoDB")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelProductoDB)

        self.lineEditProductoDB = QLineEdit(self.groupBox)
        self.lineEditProductoDB.setObjectName(u"lineEditProductoDB")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditProductoDB)

        self.labelDescripcionDB = QLabel(self.groupBox)
        self.labelDescripcionDB.setObjectName(u"labelDescripcionDB")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelDescripcionDB)

        self.lineEditDescripcionDB = QLineEdit(self.groupBox)
        self.lineEditDescripcionDB.setObjectName(u"lineEditDescripcionDB")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEditDescripcionDB)

        self.labelPrecioDB = QLabel(self.groupBox)
        self.labelPrecioDB.setText("Precio")
        self.labelPrecioDB.setObjectName(u"labelDescripcionDB")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelPrecioDB)

        self.lineEditPrecioDB = QLineEdit(self.groupBox)
        self.lineEditPrecioDB.setObjectName(u"lineEditDescripcionDB")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEditPrecioDB)

        self.labelStockDB = QLabel(self.groupBox)
        self.labelStockDB.setText("Stock")
        self.labelStockDB.setObjectName(u"labelDescripcionDB")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelStockDB)

        self.lineEditStockDB = QLineEdit(self.groupBox)
        self.lineEditStockDB.setObjectName(u"lineEditDescripcionDB")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEditStockDB)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.tablaDB = QTableView(self.tabDB)
        self.tablaDB.setObjectName(u"tablaDB")

        self.verticalLayout_5.addWidget(self.tablaDB)

        icon5 = QIcon()
        icon5.addFile(u":/CastaPC/DBIcono.png", QSize(), QIcon.Active, QIcon.On)
        self.tabWidget.addTab(self.tabDB, icon5, "")
        self.tabInformes = QWidget()
        self.tabInformes.setObjectName(u"tabInformes")
        self.verticalLayout_4 = QVBoxLayout(self.tabInformes)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.webEngineWeb = QWebEngineView(self.tabInformes)
        self.webEngineWeb.setObjectName(u"webEngineWeb")

        self.verticalLayout_4.addWidget(self.webEngineWeb)

        self.hLayoutBotonesInformes = QHBoxLayout()
        self.hLayoutBotonesInformes.setObjectName(u"hLayoutBotonesInformes")
        self.botonCompraInforme = QPushButton(self.tabInformes)
        self.botonCompraInforme.setObjectName(u"botonCompraInforme")

        self.hLayoutBotonesInformes.addWidget(self.botonCompraInforme)

        self.botonReparacionInforme = QPushButton(self.tabInformes)
        self.botonReparacionInforme.setObjectName(u"botonReparacionInforme")

        self.hLayoutBotonesInformes.addWidget(self.botonReparacionInforme)


        self.verticalLayout_4.addLayout(self.hLayoutBotonesInformes)

        icon6 = QIcon()
        icon6.addFile(u":/CastaPC/InformeIcono.png", QSize(), QIcon.Selected, QIcon.On)
        self.tabWidget.addTab(self.tabInformes, icon6, "")

        self.horizontalLayout_4.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 562, 22))
        self.menuBase_de_Datos = QMenu(self.menubar)
        self.menuBase_de_Datos.setObjectName(u"menuBase_de_Datos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuBase_de_Datos.menuAction())
        self.menuBase_de_Datos.addAction(self.actionInsertar)
        self.menuBase_de_Datos.addAction(self.actionModificar)
        self.menuBase_de_Datos.addAction(self.actionEliminar)

        self.tabWidget.addTab(self.tabComponente, "")

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionInsertar.setText(QCoreApplication.translate("MainWindow", u"Insertar", None))
#if QT_CONFIG(tooltip)
        self.actionInsertar.setToolTip(QCoreApplication.translate("MainWindow", u"Inserta datos en la base de datos.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionInsertar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionModificar.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
#if QT_CONFIG(tooltip)
        self.actionModificar.setToolTip(QCoreApplication.translate("MainWindow", u"Modifica datos en la base de datos.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionModificar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionEliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
#if QT_CONFIG(tooltip)
        self.actionEliminar.setToolTip(QCoreApplication.translate("MainWindow", u"Elimina datos en la base de datos.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionEliminar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.labelGrafica.setText("")
        self.checkBoxGrafica.setText(QCoreApplication.translate("MainWindow", u"RTX 3090 Titan 24GB", None))
        self.labelFA.setText("")
        self.checkBoxFA.setText(QCoreApplication.translate("MainWindow", u"Fuente de Alimentaci\u00f3n 850 w", None))
        self.labelProcesador.setText("")
        self.checkBoxProcesador.setText(QCoreApplication.translate("MainWindow", u"AMD Ryzen 5 3600", None))
        self.labelCaja.setText("")
        self.checkBoxCaja.setText(QCoreApplication.translate("MainWindow", u"Caja Extended ATX ", None))
        self.botonAceptarCompras.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCompras), QCoreApplication.translate("MainWindow", u"Compras", None))
        self.botonReparacion.setText(QCoreApplication.translate("MainWindow", u"Asistente", None))
        self.labelImagenReparacion.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabReparacion), QCoreApplication.translate("MainWindow", u"Reparaci\u00f3n", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Datos de Productos", None))
        self.labelIDDB.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.labelProductoDB.setText(QCoreApplication.translate("MainWindow", u"Producto", None))
        self.labelDescripcionDB.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDB), QCoreApplication.translate("MainWindow", u"Base de Datos", None))
        self.botonCompraInforme.setText(QCoreApplication.translate("MainWindow", u"Informe de Compras", None))
        self.botonReparacionInforme.setText(QCoreApplication.translate("MainWindow", u"Informe de la Reparaci\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInformes), QCoreApplication.translate("MainWindow", u"Informes", None))
        self.menuBase_de_Datos.setTitle(QCoreApplication.translate("MainWindow", u"Base de Datos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabComponente), QCoreApplication.translate("MainWindow", u"Componente", None))
    # retranslateUi

