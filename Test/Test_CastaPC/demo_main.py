import os
from pathlib import Path
import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QTabWidget, QApplication, QMainWindow, QPushButton, QWizard, QWizardPage, QLineEdit, QHBoxLayout, QLabel, QComboBox, QTextEdit, QVBoxLayout,QMessageBox, QAbstractItemView
from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
# Para ajustar el texto de los comentarios
import textwrap
# Para poner la fecha de hoy
from datetime import datetime
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel
from PySide6.QtCore import Qt,QUrl
from db2 import DB
from Graficas import Graficas
from PySide6.QtWebEngineCore import QWebEngineSettings
# from Qt import QtGui
from PySide6 import QtWidgets, QtGui
import sys

from ui_main import Ui_MainWindow
from rebotines import MainWindowRebotines
from Main_pruebas import MainWindow

basedir = os.path.dirname("CastaPC.ico")

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        mainToggle = MainWindow()
        self.setCentralWidget(mainToggle)
        
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icono.ico'))
    window = MainWindow()
    
    window.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'icono.ico')))
    window.setWindowIcon(QtGui.QIcon('icono.ico'))
    window.setWindowTitle('Casta PC')
    window.show()
    app.exec()