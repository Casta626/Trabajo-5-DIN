# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTableView, QToolBar, QVBoxLayout, QWidget)
import resources_rc_David

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionInsertar = QAction(MainWindow)
        self.actionInsertar.setObjectName(u"actionInsertar")
        icon = QIcon()
        icon.addFile(u":/icons/database--plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionInsertar.setIcon(icon)
        self.actionModificar = QAction(MainWindow)
        self.actionModificar.setObjectName(u"actionModificar")
        icon1 = QIcon()
        icon1.addFile(u":/icons/database--arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionModificar.setIcon(icon1)
        self.actionEliminar = QAction(MainWindow)
        self.actionEliminar.setObjectName(u"actionEliminar")
        icon2 = QIcon()
        icon2.addFile(u":/icons/database--minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEliminar.setIcon(icon2)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_ID = QLineEdit(self.groupBox)
        self.lineEdit_ID.setObjectName(u"lineEdit_ID")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_ID)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_Title = QLineEdit(self.groupBox)
        self.lineEdit_Title.setObjectName(u"lineEdit_Title")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_Title)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.comboBox_Artist = QComboBox(self.groupBox)
        self.comboBox_Artist.setObjectName(u"comboBox_Artist")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox_Artist)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.tabla = QTableView(self.centralwidget)
        self.tabla.setObjectName(u"tabla")

        self.verticalLayout_2.addWidget(self.tabla)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menuRegistro = QMenu(self.menubar)
        self.menuRegistro.setObjectName(u"menuRegistro")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuRegistro.menuAction())
        self.menuRegistro.addAction(self.actionInsertar)
        self.menuRegistro.addAction(self.actionModificar)
        self.menuRegistro.addAction(self.actionEliminar)
        self.toolBar.addAction(self.actionInsertar)
        self.toolBar.addAction(self.actionModificar)
        self.toolBar.addAction(self.actionEliminar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionInsertar.setText(QCoreApplication.translate("MainWindow", u"Insertar", None))
#if QT_CONFIG(shortcut)
        self.actionInsertar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionModificar.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
#if QT_CONFIG(shortcut)
        self.actionModificar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionEliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
#if QT_CONFIG(shortcut)
        self.actionEliminar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Datos del Album", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Artista", None))
        self.menuRegistro.setTitle(QCoreApplication.translate("MainWindow", u"Registro", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

