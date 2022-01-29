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

        page1.registerField('miCampo*', lineEdit,lineEdit.text(),'textChanged')
        self.wizard.addPage(page1)

        page2 = QWizardPage()
        page2.setTitle('Título de la página 2')
        page2.setSubTitle('Subtítulo de la página 2')
        label = QLabel()
        hLayout2 = QHBoxLayout(page2)
        hLayout2.addWidget(label)
        page2.setFinalPage(True)

        # Se obtiene el botón siguiente del QWizard. Listado de botones: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWizard.html#PySide6.QtWidgets.PySide6.QtWidgets.QWizard.WizardButton
        next = self.wizard.button(QWizard.NextButton)
        # Y cuando se pulsa, se conecta con una función para poner lo que ha escrito el usuario en el label de la página 2
        next.clicked.connect(lambda:label.setText(page1.field('miCampo')))

        self.wizard.addPage(page2)

    def button_clicked(self, s):
        self.wizard.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()