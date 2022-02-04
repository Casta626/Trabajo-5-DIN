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
from DB import DB

from ui_main import Ui_MainWindow
class MainWindow(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        DB.db(self)

        # Tocar checkBox y var con db y tocar los comboBox


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
        # lineEditTipoPC = QLineEdit()
        lineEditProblema = QLineEdit()
        labelProblema = QLabel()
        labelProblema.setText("Problema:")
        labelTipoPC = QLabel()
        labelTipoPC.setText("Tipo de PC:")
        self.combopc = QComboBox()
        self.combopc.addItem("Sobremesa")
        self.combopc.addItem("Portátil")
        hLayoutP1 = QHBoxLayout(page1)
        hLayoutP1.addWidget(labelTipoPC)
        hLayoutP1.addWidget(self.combopc)
        # hLayoutP1.addWidget(lineEditTipoPC)
        hLayoutP1.addWidget(labelProblema)
        hLayoutP1.addWidget(lineEditProblema)
        
        page1.registerField('problema*', lineEditProblema,lineEditProblema.text(),'textChanged')
        self.wizard.addPage(page1)
        
         

        page2 = QWizardPage()
        page2.setTitle('Sobre su problema')
        page2.setSubTitle('¿Cree que necesitaria nuevas piezas?')
        label = QLabel()
        labelPiezas = QLabel()
        labelPiezas.setText("¿Creé que necesitaría nuevas piezas?")
        
        
        self.comboPiezas = QComboBox()
        self.comboPiezas.addItem("No sé")
        self.comboPiezas.addItem("Sí")
        self.comboPiezas.addItem("No")
        vLayoutP2 = QVBoxLayout(page2)
        
        vLayoutP2.addWidget(label)
        vLayoutP2.addWidget(labelPiezas)
        vLayoutP2.addWidget(self.comboPiezas)
        
        # page2.registerField('piezas*', lineEditPiezas,lineEditPiezas.text(),'textChanged')

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
        
        self.comboDias = QComboBox()
        self.comboDias.addItem("1 Día laboral")
        self.comboDias.addItem("3 Días laborales")
        self.comboDias.addItem("5 Días laborales")
        hLayoutP3 = QHBoxLayout(page3)
        hLayoutP3.addWidget(labelDias)
        hLayoutP3.addWidget(lineEditDias)
        hLayoutP3.addWidget(self.comboDias)

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
        self.label1 = QLabel()
        labelT2 = QLabel()
        labelT2.setText("Problema: ")
        self.label2 = QLabel()
        labelT3 = QLabel()
        labelT3.setText("Piezas nuevas: ")
        self.label3 = QLabel()
        labelT4 = QLabel()
        labelT4.setText("Rapidez: ")
        self.label4 = QLabel()
        labelT5 = QLabel()
        labelT5.setText("Comentarios: ")
        self.label5 = QLabel()
        labelT6 = QLabel()
        labelT6.setText("Prueba comboBox: ")
        self.label6 = QLabel()
        self.label6.setText(str(self.comboPiezas.currentText()))
        
        vLayoutP5 = QVBoxLayout(page5)
        hLayoutP5 = QHBoxLayout()
        hLayout2P5 = QHBoxLayout()
        hLayoutP5.addWidget(labelT1)
        hLayoutP5.addWidget(self.label1)
        hLayoutP5.addWidget(labelT2)
        hLayoutP5.addWidget(self.label2)
        hLayoutP5.addWidget(labelT3)
        hLayoutP5.addWidget(self.label3)
        hLayoutP5.addWidget(labelT4)
        hLayoutP5.addWidget(self.label4) 
        hLayoutP5.addWidget(labelT5)
        hLayout2P5.addWidget(self.label5)
        hLayout2P5.addWidget(self.label6)
        vLayoutP5.addLayout(hLayoutP5)
        vLayoutP5.addLayout(hLayout2P5)
        


        self.wizard.addPage(page5)

        # next.clicked.connect(lambda:self.label1.setText(page5.field('tipoPC')))
        next.clicked.connect(lambda:self.label2.setText(page5.field('problema')))
        next.clicked.connect(lambda:self.label3.setText(page5.field('piezas')))
        next.clicked.connect(lambda:self.label4.setText(page5.field('dias')))
        next.clicked.connect(lambda:self.label5.setText(page5.field('comentarios')))

        

        page5.setFinalPage(True)

        finish = self.wizard.button(QWizard.FinishButton)

        finish.clicked.connect(self.generaPDFwizard)

        # finish = self.wizard.button(QWizard.FinishButton)
        # finish.clicked.connect(lambda:label.setText("Según su problema: "+page1.field('problema')))


        self.pushButton2.clicked.connect(self.iniciarWizard)

        

    # Codigo db en caso de emergencia.

    def iniciarWizard(self):
        self.wizard.show()


    def generaPDFwizard(self):
    
        outfile = "result.pdf"

        template = PdfReader("template.pdf", decompress=False).pages[0]
        template_obj = pagexobj(template)

        canvas = Canvas(outfile)

        xobj_name = makerl(canvas, template_obj)
        canvas.doForm(xobj_name)

        ystart = 455

        canvas.drawString(122, ystart, self.label1.text())

        # Ponemos la fecha de hoy
        today = datetime.today()
        canvas.drawString(455, ystart, today.strftime('%F'))

        # Lo ideal es partir de una posición y jugar con el tamaño de la fuente
        # En este caso, cada línea son 28 puntos
        canvas.drawString(294, ystart, self.label2.text())
        # canvas.drawString(230, ystart-28, self.data['apellidos'])

        canvas.drawString(175, ystart-(32), self.label3.text())

        canvas.drawString(290, ystart-(32), self.label4.text())

        canvas.drawString(423, ystart-(32), self.comboPiezas.currentText())

        # canvas.drawString(168, ystart-(2*32), self.data['n_perifericos'])

        # canvas.drawString(285, ystart-(2*32), self.data['perifericos'])

        # canvas.drawString(128, ystart-(3*32), self.data['direccion'])

        canvas.drawString(472, ystart-(3*32), "Python")

        # canvas.drawString(472, ystart-(2*32), self.data['prueba'])

        # Sería posible establecer un límite en el número de caracteres:
        # field.setMaxLength(25)

        # Reemplazamos los saltos de línea por espacios en los comentarios
        comments = self.label5.text().replace('\n', ' ')
        if comments:
            # Separamos el texto de la primera línea (más corta que el resto)
            lines = textwrap.wrap(comments, width=65)
            # Nos quedamos la primera línea
            first_line = lines[0]
            # Guardamos el resto en remainder
            remainder = ' '.join(lines[1:])

            # Separamos el resto con una anchura mayot
            lines = textwrap.wrap(remainder, 75)
            # Nos quedamos con las cuatro primeras que son el máximo (sin incluir la primera)
            lines = lines[:4]

            # Escribimos la primera línea
            canvas.drawString(147, ystart-(4*32), first_line)
            # Y luego las otras cuatro
            for n, l in enumerate(lines, 1):
                canvas.drawString(80, ystart-(4*32) - (n*32), l)

        canvas.save()
        QMessageBox.information("Finalizado", "Se ha generado el PDF")

        

    def button_clicked(self, s):
        self.wizard.show()

    def atras(self):
        # app.closeAllWindows()
        self.close()
	    # self.wizard.close()

app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle('Casta PC')
window.show()
app.exec()