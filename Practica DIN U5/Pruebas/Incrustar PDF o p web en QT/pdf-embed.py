import sys
from pathlib import Path
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWizard, QWizardPage, QLineEdit, QHBoxLayout, QLabel
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi aplicación")

        # QWebEngineView es una vista de una web (vista de un navegador incrustada en una app)
        # Documentación de la clase: https://doc.qt.io/qtforpython/PySide6/QtWebEngineWidgets/QWebEngineView.html
        self.web = QWebEngineView()

        # Para mostrar un PDF, es necesario habilitar los plugins. Los plugins están en https://doc.qt.io/qtforpython/PySide6/QtWebEngineCore/QWebEngineSettings.html#detailed-description
        self.web.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

        # Con Path guardamos la ruta relativa al documento
        rutaConPDF = Path("template.pdf")
        # Cargamos el fichero con la ruta absoluta como uri
        # Usando http o https también se pueden cargar páginas web
        self.web.load(QUrl(rutaConPDF.absolute().as_uri()))

        self.setCentralWidget(self.web)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()