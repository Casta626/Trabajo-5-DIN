from Main import MainWindow
from ui_main import Ui_MainWindow
from Main import MainWindow
from PySide6.QtWidgets import QMainWindow, QPushButton, QWizard, QWizardPage, QLineEdit, QHBoxLayout, QLabel, QComboBox, QTextEdit, QVBoxLayout,QMessageBox
from PySide6.QtGui import QPixmap

class Wizard(MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    
        
    # self.button = QPushButton("Presióname para un Wizard")
        # self.button.clicked.connect(self.button_clicked)
        
        
        # self.button2 = QPushButton("Salir del asistente")
        # self.button2.clicked.connect(self.atras)
        
        # self.QH1 = QHBoxLayout()
        # self.QH1.addWidget(self.button)
        # self.QH1.addWidget(self.button2)

        


        self.wizard = QWizard()
        

        self.wizard.setWizardStyle(QWizard.ModernStyle)

        self.wizard.setPixmap(QWizard.WatermarkPixmap,QPixmap('marcadeagua.png'))
        self.wizard.setPixmap(QWizard.LogoPixmap,QPixmap('icono.png'))
        self.wizard.setPixmap(QWizard.BannerPixmap,QPixmap('Banner.png'))

        # self.setCentralWidget(self.wizard)

        page1 = QWizardPage()
        page1.setTitle('Reparación')
        page1.setSubTitle('Seleccione su tipo de ordenador y comente su problema brevemente')
        lineEditTipoPC = QLineEdit()
        lineEditProblema = QLineEdit()
        labelProblema = QLabel()
        labelProblema.setText("Problema")
        labelTipoPC = QLabel()
        labelTipoPC.setText("Tipo de PC")
        # combopc = QComboBox()
        # combopc.addItem("Sobremesa")
        # combopc.addItem("Portátil")
        hLayoutP1 = QHBoxLayout(page1)
        # hLayout1.addWidget(combopc)
        hLayoutP1.addWidget(labelTipoPC)
        hLayoutP1.addWidget(lineEditTipoPC)
        hLayoutP1.addWidget(labelProblema)
        hLayoutP1.addWidget(lineEditProblema)
        

        page1.registerField('tipoPC*', lineEditTipoPC,lineEditTipoPC.text(),'textChanged')
        page1.registerField('problema*', lineEditProblema,lineEditProblema.text(),'textChanged')
        # page1.registerField('tipoPC*', combopc,combopc.currentText(),'setText')
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
        labelPiezas = QLabel()
        labelPiezas.setText("¿Necesitaría nuevas piezas?")
        lineEditPiezas = QLineEdit()
        
        # comboPiezas = QComboBox()
        # comboPiezas.addItem("No sé")
        # comboPiezas.addItem("Sí")
        # comboPiezas.addItem("No")
        vLayoutP2 = QVBoxLayout(page2)
        
        vLayoutP2.addWidget(label)
        vLayoutP2.addWidget(lineEditPiezas)
        # vLayout2.addWidget(comboPiezas)
        
        page2.registerField('piezas*', lineEditPiezas,lineEditPiezas.text(),'textChanged')

        self.wizard.addPage(page2)

         # Se obtiene el botón siguiente del QWizard. Listado de botones: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWizard.html#PySide6.QtWidgets.PySide6.QtWidgets.QWizard.WizardButton
        next = self.wizard.button(QWizard.NextButton)
        
        # cancel = self.wizard.button(QWizard.CancelButton)
        # Y cuando se pulsa, se conecta con una función para poner lo que ha escrito el usuario en el label de la página 2
        next.clicked.connect(lambda:label.setText("Según su problema: "+page1.field('problema')))
        # cancel.clicked.connect(self.atras)

        page3 = QWizardPage()
        page3.setTitle('Rapidez')
        page3.setSubTitle('Indique en cuantos días le gustaría tener arreglado el problema')
        labelDias = QLabel()
        labelDias.setText("Días laborales:")
        lineEditDias = QLineEdit()
        
        # comboDias = QComboBox()
        # comboDias.addItem("1 Día laboral")
        # comboDias.addItem("3 Días laborales")
        # comboDias.addItem("5 Días laborales")
        hLayoutP3 = QHBoxLayout(page3)
        hLayoutP3.addWidget(labelDias)
        hLayoutP3.addWidget(lineEditDias)
        # hLayout3.addWidget(comboDias)

        page3.registerField('dias*', lineEditDias,lineEditDias.text(),'textChanged')

        self.wizard.addPage(page3)

        

        page4 = QWizardPage()
        page4.setTitle('Comentarios')
        page4.setSubTitle('Indique la información adicional que quiera')
        lineEditComentarios = QLineEdit()
        hLayoutP4 = QHBoxLayout(page4)
        hLayoutP4.addWidget(lineEditComentarios) 

        page4.registerField('comentarios*', lineEditComentarios,lineEditComentarios.text(),'textChanged')

        self.wizard.addPage(page4)
        
        
        self.wizard.setWindowTitle("Asistente CastaPC")

        

        page5 = QWizardPage()
        page5.setTitle('Resumen')
        page5.setSubTitle('Confirme que estos datos son correctos para imprimirlos')
        labelT1 = QLabel()
        labelT1.setText("Tipo de PC: ")
        label1 = QLabel()
        labelT2 = QLabel()
        labelT2.setText("Problema: ")
        label2 = QLabel()
        labelT3 = QLabel()
        labelT3.setText("Piezas nuevas: ")
        label3 = QLabel()
        labelT4 = QLabel()
        labelT4.setText("Rapidez: ")
        label4 = QLabel()
        labelT5 = QLabel()
        labelT5.setText("Comentarios: ")
        label5 = QLabel()
        
        vLayoutP5 = QVBoxLayout(page5)
        hLayoutP5 = QHBoxLayout()
        hLayout2P5 = QHBoxLayout()
        hLayoutP5.addWidget(labelT1)
        hLayoutP5.addWidget(label1)
        hLayoutP5.addWidget(labelT2)
        hLayoutP5.addWidget(label2)
        hLayoutP5.addWidget(labelT3)
        hLayoutP5.addWidget(label3)
        hLayoutP5.addWidget(labelT4)
        hLayoutP5.addWidget(label4) 
        hLayoutP5.addWidget(labelT5)
        hLayout2P5.addWidget(label5)
        vLayoutP5.addLayout(hLayoutP5)
        vLayoutP5.addLayout(hLayout2P5)
        


        self.wizard.addPage(page5)

        next.clicked.connect(lambda:label1.setText(page5.field('tipoPC')))
        next.clicked.connect(lambda:label2.setText(page5.field('problema')))
        next.clicked.connect(lambda:label3.setText(page5.field('piezas')))
        next.clicked.connect(lambda:label4.setText(page5.field('dias')))
        next.clicked.connect(lambda:label5.setText(page5.field('comentarios')))

        page5.setFinalPage(True)

        self.wizard.show()
