from Main import MainWindow
from ui_main import Ui_MainWindow
from Main import MainWindow
import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWizard, QWizardPage, QLineEdit, QHBoxLayout, QLabel, QComboBox, QTextEdit, QVBoxLayout,QMessageBox, QAbstractItemView
from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
# Para ajustar el texto de los comentarios
import textwrap
# Para poner la fecha de hoy
from datetime import datetime
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel
from PySide6.QtCore import Qt

class GenWizard(MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    