import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWizard, QWizardPage, QLineEdit, QHBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi aplicación")

        self.button = QPushButton("Presióname para un Wizard")
        self.button.clicked.connect(self.button_clicked)
        self.setCentralWidget(self.button)
        
        # Creamos un QWizard
        self.wizard = QWizard()

        # Establecemos un estilo del QWizard
        self.wizard.setWizardStyle(QWizard.ModernStyle)

        # Se pueden ver los estilos en https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWizard.html#PySide6.QtWidgets.PySide6.QtWidgets.QWizard.setWizardStyle
                # self.wizard.setWizardStyle(QWizard.AeroStyle)
        # self.wizard.setWizardStyle(QWizard.ClassicStyle)
                # self.wizard.setWizardStyle(QWizard.MacStyle)

        # Podemos poner diferentes tipos de imágenes (dependiendo del estilo del QWizard)
        self.wizard.setPixmap(QWizard.WatermarkPixmap,QPixmap('Watermark.png'))
        self.wizard.setPixmap(QWizard.LogoPixmap,QPixmap('Logo.png'))
        self.wizard.setPixmap(QWizard.BannerPixmap,QPixmap('Banner.png'))

        # Un QWizard se compone de páginas QWizardPage con elementos: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWizard.html#elements-of-a-wizard-page
        page1 = QWizardPage()
        page1.setTitle('Título de la página 1')
        page1.setSubTitle('Subtítulo de la página 1')
        lineEdit = QLineEdit()
        hLayout1 = QHBoxLayout(page1)
        hLayout1.addWidget(lineEdit)

        # Añadimos la página al QWizard, como se hace con los widgets en los layouts
        self.wizard.addPage(page1)

    def button_clicked(self, s):
        # Mostramos el QWizard al pulsar el botón
        self.wizard.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()