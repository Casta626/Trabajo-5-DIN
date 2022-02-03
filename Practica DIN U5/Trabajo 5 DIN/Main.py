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

from ui_app import Ui_MainWindow
class MainWindow(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton2.clicked.connect(self.iniciarWizard)

        # Realizamos la carga y apertura de la base de datos
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("chinook.sqlite")

        db.open()
        # Creamos una query para obtener todos los artistas de la tabla Artist
        query = QSqlQuery("SELECT Name FROM Artist",db=db)
        # Recorremos el resultado de esa query agregando al comboBox el listado de artistas
        # while query.next():
        #     self.comboBox_Artist.addItem(query.value(0))

        # Creamos un modelo relacional de SQL
        self.modelo = QSqlRelationalTableModel(db=db)
        # Establecemos Album como tabla del modelo
        self.modelo.setTable("Album")
        # Establecemos la relación entre el ID de los artistas y su nombre, para que se muestre este último
        self.modelo.setRelation(2, QSqlRelation("Artist", "ArtistId", "Name"))
        # Hacemos el select del modelo
        self.modelo.select()
        # Renombramos las cabeceras de la tabla
        self.modelo.setHeaderData(0, Qt.Horizontal, "Id")
        self.modelo.setHeaderData(1, Qt.Horizontal, "Título")
        self.modelo.setHeaderData(2, Qt.Horizontal, "Artista")

        # Establecemos el modelo en el tableView
        self.tableView.setModel(self.modelo)
        # Ajustamos el tamaño de las columnas al contenido
        self.tableView.resizeColumnsToContents()

        # Deshabilitamos la edición directa de la tabla
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Establecemos que se seleccionen filas completas en lugar de celdas individuales
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Creamos la señal: Cuando cambie la seleccion, ejecuta self.seleccion
        # self.tableView.selectionModel().selectionChanged.connect(self.seleccion)
        # # Creamos la señal: Cuando se ejecute la acción Modificar, ejecuta self.modificar
        # self.actionModificar.triggered.connect(self.modificar)
        # # Creamos la señal: Cuando se ejecute la acción Insertar, ejecuta self.nueva
        # self.actionInsertar.triggered.connect(self.nueva)
        # # Creamos la señal: Cuando se ejecute la acción Eliminar, ejecuta self.borrar
        # self.actionEliminar.triggered.connect(self.borrar)

        # Ponemos la fila inicial a un valor que indica que no está seleccionada ninguna fila
        self.fila = -1
        

    def iniciarWizard(self):
        
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
        
        self.wizard.show()
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



        finish = self.wizard.button(QWizard.FinishButton)
        # finish.clicked.connect(lambda:label.setText("Según su problema: "+page1.field('problema')))
    
        outfile = "result.pdf"

        template = PdfReader("template.pdf", decompress=False).pages[0]
        template_obj = pagexobj(template)

        canvas = Canvas(outfile)

        xobj_name = makerl(canvas, template_obj)
        canvas.doForm(xobj_name)

        ystart = 455

        canvas.drawString(122, ystart, label1.text())

        # Ponemos la fecha de hoy
        today = datetime.today()
        canvas.drawString(455, ystart, today.strftime('%F'))

        # Lo ideal es partir de una posición y jugar con el tamaño de la fuente
        # En este caso, cada línea son 28 puntos
        canvas.drawString(294, ystart, label2.text())
        # canvas.drawString(230, ystart-28, self.data['apellidos'])

        canvas.drawString(175, ystart-(32), label3.text())

        canvas.drawString(290, ystart-(32), label4.text())

        # canvas.drawString(423, ystart-(32), label5.text())

        # canvas.drawString(168, ystart-(2*32), self.data['n_perifericos'])

        # canvas.drawString(285, ystart-(2*32), self.data['perifericos'])

        # canvas.drawString(128, ystart-(3*32), self.data['direccion'])

        canvas.drawString(472, ystart-(3*32), "Python")

        # canvas.drawString(472, ystart-(2*32), self.data['prueba'])

        # Sería posible establecer un límite en el número de caracteres:
        # field.setMaxLength(25)

        # Reemplazamos los saltos de línea por espacios en los comentarios
        comments = label5.text().replace('\n', ' ')
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
        QMessageBox.information(self, "Finalizado", "Se ha generado el PDF")

        finish = self.wizard.button(QWizard.FinishButton)

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