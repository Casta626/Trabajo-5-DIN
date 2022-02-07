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
        
        self.wizard = QWizard()

        self.wizard.setWizardStyle(QWizard.ModernStyle)

        self.wizard.setPixmap(QWizard.WatermarkPixmap,QPixmap('Watermark.png'))
        self.wizard.setPixmap(QWizard.LogoPixmap,QPixmap('Logo.png'))
        self.wizard.setPixmap(QWizard.BannerPixmap,QPixmap('Banner.png'))

        page1 = QWizardPage()
        page1.setTitle('Título de la página 1')
        page1.setSubTitle('Subtítulo de la página 1')
        lineEdit = QLineEdit()
        hLayout1 = QHBoxLayout(page1)
        hLayout1.addWidget(lineEdit)

        # Normalmente guardaremos la información que introduce el usuario para utilizarla
        # registerField(nombre_campo, widget, info_a_guardar)
        page1.registerField('miCampo', lineEdit,lineEdit.text())
        # Se accede al campo usando page1.field('miCampo')

        # Podemos hacer el campo obligatorio poniendo un * (el botón de Siguiente se bloqueará)
        # También debemos añadir la señal del componente que emite cuando se actualiza para comprobarlo
        #page1.registerField('miCampo', lineEdit,lineEdit.text(),'textChanged')
        self.wizard.addPage(page1)

        page2 = QWizardPage()
        page2.setTitle('Título de la página 2')
        page2.setSubTitle('Subtítulo de la página 2')
        label = QLabel("Este es el texto de la página 2.")
        hLayout2 = QHBoxLayout(page2)
        hLayout2.addWidget(label)
        page2.setFinalPage(True)
        self.wizard.addPage(page2)

    def button_clicked(self, s):
        self.wizard.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()