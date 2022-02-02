import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWizard, QWizardPage, QLineEdit, QHBoxLayout, QLabel, QComboBox, QTextEdit, QVBoxLayout
from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem, QMainWindow, QPushButton

from ui_app import Ui_MainWindow
class MainWindow(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton2.clicked.connect(self.iniciarWizard)
        
        

    def iniciarWizard(self):
        
        self.button = QPushButton("Presióname para un Wizard")
        self.button.clicked.connect(self.button_clicked)
        
        
        self.button2 = QPushButton("Salir del asistente")
        self.button2.clicked.connect(self.atras)
        
        self.QH1 = QHBoxLayout()
        self.QH1.addWidget(self.button)
        self.QH1.addWidget(self.button2)

        


        self.wizard = QWizard()
        

        self.wizard.setWizardStyle(QWizard.ModernStyle)

        self.wizard.setPixmap(QWizard.WatermarkPixmap,QPixmap('Watermark.png'))
        self.wizard.setPixmap(QWizard.LogoPixmap,QPixmap('CastaPC.png'))
        self.wizard.setPixmap(QWizard.BannerPixmap,QPixmap('Banner.png'))

        # self.setCentralWidget(self.wizard)

        page1 = QWizardPage()
        page1.setTitle('Reparación')
        page1.setSubTitle('Seleccione su tipo de ordenador y comente su problema brevemente')
        lineEdit = QLineEdit()
        combopc = QComboBox()
        combopc.addItem("Sobremesa")
        combopc.addItem("Portátil")
        hLayout1 = QHBoxLayout(page1)
        hLayout1.addWidget(combopc)
        hLayout1.addWidget(lineEdit)
        

        page1.registerField('miCampo*', lineEdit,lineEdit.text(),'textChanged')
        self.wizard.addPage(page1)

        # page1 = QWizardPage()
        # page1.setTitle('Reparación')
        # page1.setSubTitle('Seleccione su tipo de ordenador y comente su problema')
        # textEdit = QTextEdit()
        # combopc = QComboBox()
        # combopc.addItem("Sobremesa")
        # combopc.addItem("Portátil")
        # hLayout1 = QHBoxLayout(page1)
        # hLayout1.addWidget(combopc)
        # hLayout1.addWidget(textEdit)
        

        # page1.registerField('miCampo*', textEdit,textEdit.toPlainText(),'textChanged')
        # self.wizard.addPage(page1)

        
         

        page2 = QWizardPage()
        page2.setTitle('Sobre su problema')
        page2.setSubTitle('¿Cree que necesitaria nuevas piezas?')
        label = QLabel()
        comboPiezas = QComboBox()
        comboPiezas.addItem("No se")
        comboPiezas.addItem("Sí")
        comboPiezas.addItem("No")
        vLayout2 = QVBoxLayout(page2)
        
        vLayout2.addWidget(label)
        vLayout2.addWidget(comboPiezas)

        self.wizard.addPage(page2)

         # Se obtiene el botón siguiente del QWizard. Listado de botones: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWizard.html#PySide6.QtWidgets.PySide6.QtWidgets.QWizard.WizardButton
        next = self.wizard.button(QWizard.NextButton)
        # cancel = self.wizard.button(QWizard.CancelButton)
        # Y cuando se pulsa, se conecta con una función para poner lo que ha escrito el usuario en el label de la página 2
        next.clicked.connect(lambda:label.setText("Según su problema: "+page1.field('miCampo')))
        # cancel.clicked.connect(self.atras)

        page3 = QWizardPage()
        page3.setTitle('Rapidez')
        page3.setSubTitle('Indique en cuantos días le gustaría tener arreglado el problema')
        label2 = QLabel()
        comboDias = QComboBox()
        comboDias.addItem("1 Día laboral")
        comboDias.addItem("3 Días laborales")
        comboDias.addItem("5 Días laborales")
        hLayout3 = QHBoxLayout(page3)
        hLayout3.addWidget(label2)
        hLayout3.addWidget(comboDias)
        self.wizard.addPage(page3)

        page4 = QWizardPage()
        page4.setTitle('Comentarios')
        page4.setSubTitle('Indique la información adicional que quiera')
        textEdit = QTextEdit()
        hLayout4 = QHBoxLayout(page4)
        hLayout4.addWidget(textEdit) 
        self.wizard.addPage(page4)

        page4.setFinalPage(True)
        
        self.wizard.show()
        self.wizard.setWindowTitle("Asistente CastaPC")

    def button_clicked(self, s):
        self.wizard.show()

    def atras(self):
        app.closeAllWindows()
        # self.close()
	    # self.wizard.close()

app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle('Casta PC')
window.show()
app.exec()