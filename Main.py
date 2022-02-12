from pathlib import Path
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
from PySide6.QtCore import Qt,QUrl
from DB import DB
from Graficas import Graficas
from PySide6.QtWebEngineCore import QWebEngineSettings


from pruebaDefinitiva2 import Ui_MainWindow
class MainWindow(DB,QMainWindow,Ui_MainWindow):

    def contadorProductos(self):
        self.precioTotal = 0
        self.datosCheckBox = ""
        if self.checkBoxCaja.isChecked():
            self.datosCheckBox += self.idCaja+" "
            self.precioTotal += self.idCajaPrecio

        if self.checkBoxGrafica.isChecked():
            self.datosCheckBox += self.idGrafica+" "
            self.precioTotal += self.idGraficaPrecio

        if self.checkBoxProcesador.isChecked():
            self.datosCheckBox += self.idProcesador+" "
            self.precioTotal += self.idProcesadorPrecio

        if self.checkBoxFA.isChecked():
            self.datosCheckBox += self.idFA
            self.precioTotal += self.idFAPrecio

        print(self.datosCheckBox)
        print(self.precioTotal)
        self.datosPrecioTotal = self.precioTotal
        self.datosProductosTotal = self.datosCheckBox

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        DB.lanzarDB(self)

        DB.generaImgGrafica(self)

        self.mostrarCompraPDF()

        self.botonCompraInforme.clicked.connect(self.mostrarCompraPDF)
        self.botonReparacionInforme.clicked.connect(self.mostrarReparacionPDF)

        self.botonAceptarCompras.clicked.connect(self.contadorProductos)


        self.datosPrecioTotal = 0

        self.datosProductosTotal = ""
   
            # https://www.youtube.com/watch?v=vJlQ1pfETIo


        
    

        # Tocar checkBox para igualarlo a sus correspondientes en la base de datos
        # y tocar la base de datos para tenerla como David


#################################    Wizard de Compra   #########################################
        self.wizardCompra = QWizard()
        

        self.wizardCompra.setWizardStyle(QWizard.ModernStyle)

        self.wizardCompra.setPixmap(QWizard.WatermarkPixmap,QPixmap('marcadeagua.png'))
        self.wizardCompra.setPixmap(QWizard.LogoPixmap,QPixmap('icono.png'))
        # self.wizardCompra.setPixmap(QWizard.BannerPixmap,QPixmap('CastaSoftIndustries.png'))


        nextWC = self.wizardCompra.button(QWizard.NextButton)
        nextWC.clicked.connect(self.actualizarDatosWizardCompra)

        finishWC = self.wizardCompra.button(QWizard.FinishButton)

        finishWC.clicked.connect(self.generaPDFwizardCompra)


        self.pagina1 = QWizardPage()
        self.pagina1.setTitle('Compras')
        self.pagina1.setSubTitle('Una vez seleccionado lo articulos rellene los siguientes campos:')
       
        self.labelNombre = QLabel()
        self.labelNombre.setText("Nombre: ")
        self.lineEditNombre = QLineEdit()
        self.labelApellido1 = QLabel()
        self.labelApellido1.setText("Primer Apellido: ")
        self.lineEditApellido1 = QLineEdit()
        self.labelApellido2 = QLabel()
        self.labelApellido2.setText("Segundo Apellido: ")
        self.lineEditApellido2 = QLineEdit()
        self.labelCorreo = QLabel()
        self.labelCorreo.setText("Correo electrónico: ")
        self.lineEditCorreo = QLineEdit()
        self.labelEdad = QLabel()
        self.labelEdad.setText("Edad: ")
        self.lineEditEdad = QLineEdit()

        self.vLayoutCompra = QVBoxLayout(self.pagina1)
        hLayoutCompra = QHBoxLayout()
        vLayoutCompra2 = QVBoxLayout()
        vLayoutCompra2.addWidget(self.labelNombre)
        vLayoutCompra2.addWidget(self.lineEditNombre)
        vLayoutCompra2.addWidget(self.labelApellido1)
        vLayoutCompra2.addWidget(self.lineEditApellido1)
        vLayoutCompra2.addWidget(self.labelApellido2)
        vLayoutCompra2.addWidget(self.lineEditApellido2)
        vLayoutCompra2.addWidget(self.labelCorreo)
        vLayoutCompra2.addWidget(self.lineEditCorreo) 
        vLayoutCompra2.addWidget(self.labelEdad)
        hLayoutCompra.addWidget(self.lineEditEdad)
        self.vLayoutCompra.addLayout(vLayoutCompra2)
        self.vLayoutCompra.addLayout(hLayoutCompra)

        self.botonAceptarCompras.clicked.connect(self.iniciarWizardCompra)
        

        self.wizardCompra.addPage(self.pagina1)


        self.pagina2 = QWizardPage()
        self.pagina2.setTitle('Forma de pago')
        self.pagina2.setSubTitle('Introduzca su tarjeta de débito o crédito')

        self.labelTarjeta = QLabel()
        self.labelTarjeta.setText("Número de la tarjeta:")
        self.lineEditTarjeta = QLineEdit()
        self.labelfechaCaducidadTarjeta = QLabel()
        self.labelfechaCaducidadTarjeta.setText("Fecha caduca:")
        self.lineEditfechaCaducidadTarjeta = QLineEdit()
        self.labelCVV = QLabel()
        self.labelCVV.setText("CVV:")
        self.lineEditCVV = QLineEdit()

        self.hLayoutPago1 = QHBoxLayout()
        self.hLayoutPago1.addWidget(self.labelTarjeta)
        self.hLayoutPago1.addWidget(self.lineEditTarjeta)
        self.hLayoutPago2 = QHBoxLayout()
        self.hLayoutPago2.addWidget(self.labelfechaCaducidadTarjeta)
        self.hLayoutPago2.addWidget(self.lineEditfechaCaducidadTarjeta)
        self.hLayoutPago2.addWidget(self.labelCVV)
        self.hLayoutPago2.addWidget(self.lineEditCVV)
        self.vLayoutPago1 = QVBoxLayout(self.pagina2)
        self.vLayoutPago1.addLayout(self.hLayoutPago1)
        self.vLayoutPago1.addLayout(self.hLayoutPago2)

        self.wizardCompra.addPage(self.pagina2)


        self.pagina3 = QWizardPage()
        self.pagina3.setTitle('Resumen')
        self.pagina3.setSubTitle('Confirme que estos datos son correctos, para imprimirlos pulse finish')

        self.nombre = QLabel()
        self.nombre.setText("Nombre: ")
        self.labelGetNombre = QLabel()
        self.labelGetNombre.setText(str(self.lineEditNombre.text()))
        
        self.apellido1 = QLabel()
        self.apellido1.setText("Apellido 1: ")
        self.labelGetApellido1 = QLabel()
        self.labelGetApellido1.setText(str(self.lineEditApellido1.text()))

        self.apellido2 = QLabel()
        self.apellido2.setText("Apellido 2: ")
        self.labelGetApellido2 = QLabel()
        self.labelGetApellido2.setText(str(self.lineEditApellido2.text()))

        self.correo = QLabel()
        self.correo.setText("Correo: ")
        self.labelGetCorreo = QLabel()
        self.labelGetCorreo.setText(str(self.lineEditCorreo.text()))

        self.edad = QLabel()
        self.edad.setText("Edad: ")
        self.labelGetEdad = QLabel()
        self.labelGetEdad.setText(str(self.lineEditEdad.text()))

        self.tarjeta = QLabel()
        self.tarjeta.setText("Tarjeta: ")
        self.labelGetTarjeta = QLabel()
        self.labelGetTarjeta.setText(str(self.lineEditTarjeta.text()))

        self.fechaCaducidadTarjeta = QLabel()
        self.fechaCaducidadTarjeta.setText("Fecha de caducidad: ")
        self.labelGetFechaCaducidadTarjeta = QLabel()
        self.labelGetFechaCaducidadTarjeta.setText(str(self.lineEditfechaCaducidadTarjeta.text()))

        self.cvv = QLabel()
        self.cvv.setText("CVV: ")
        self.labelGetCVV = QLabel()
        self.labelGetCVV.setText(str(self.lineEditCVV.text()))

        self.labelDatosNombre = QLabel()
        self.labelDatosNombre.setText("Datos del usuario:")

        self.labelDatosTarjeta = QLabel()
        self.labelDatosTarjeta.setText("Datos de la tarjeta del usuario:")


        self.centralvLayoutCompraP3 = QVBoxLayout(self.pagina3)
        self.centralvLayoutCompraP3.addWidget(self.labelDatosNombre)

        self.hLayoutCompraP3 = QHBoxLayout()
        self.hLayoutCompraP3.addWidget(self.nombre)
        self.hLayoutCompraP3.addWidget(self.labelGetNombre)
        self.centralvLayoutCompraP3.addLayout(self.hLayoutCompraP3)

        self.hLayout2CompraP3 = QHBoxLayout()
        self.hLayout2CompraP3.addWidget(self.apellido1)
        self.hLayout2CompraP3.addWidget(self.labelGetApellido1)
        self.centralvLayoutCompraP3.addLayout(self.hLayout2CompraP3)

        self.hLayout3CompraP3 = QHBoxLayout()
        self.hLayout3CompraP3.addWidget(self.apellido2)
        self.hLayout3CompraP3.addWidget(self.labelGetApellido2)
        self.centralvLayoutCompraP3.addLayout(self.hLayout3CompraP3)

        self.hLayout4CompraP3 = QHBoxLayout()
        self.hLayout4CompraP3.addWidget(self.correo)
        self.hLayout4CompraP3.addWidget(self.labelGetCorreo)
        self.centralvLayoutCompraP3.addLayout(self.hLayout4CompraP3)

        self.hLayout5CompraP3 = QHBoxLayout()
        self.hLayout5CompraP3.addWidget(self.edad)
        self.hLayout5CompraP3.addWidget(self.labelGetEdad)
        self.centralvLayoutCompraP3.addLayout(self.hLayout5CompraP3)

        self.centralvLayoutCompraP3.addWidget(self.labelDatosTarjeta)

        self.hLayout6CompraP3 = QHBoxLayout()
        self.hLayout6CompraP3.addWidget(self.tarjeta)
        self.hLayout6CompraP3.addWidget(self.labelGetTarjeta)
        self.centralvLayoutCompraP3.addLayout(self.hLayout6CompraP3)

        self.hLayout7CompraP3 = QHBoxLayout()
        self.hLayout7CompraP3.addWidget(self.fechaCaducidadTarjeta)
        self.hLayout7CompraP3.addWidget(self.labelGetFechaCaducidadTarjeta)
        self.centralvLayoutCompraP3.addLayout(self.hLayout7CompraP3)

        self.hLayout8CompraP3 = QHBoxLayout()
        self.hLayout8CompraP3.addWidget(self.cvv)
        self.hLayout8CompraP3.addWidget(self.labelGetCVV)
        self.centralvLayoutCompraP3.addLayout(self.hLayout8CompraP3)


        # self.hLayoutCompraP3 = QHBoxLayout()
        # self.hLayoutCompraP3.addWidget(self.label1)

        # self.hLayout2CompraP3 = QHBoxLayout()
        # self.hLayout2CompraP3.addWidget(self.label5)
        # self.hLayout2CompraP3.addWidget(self.label5)

        # self.centralvLayoutCompraP3.addLayout(self.hLayoutCompraP3)
        # self.centralvLayoutCompraP3.addLayout(self.hLayout2CompraP3)
        

        self.wizardCompra.addPage(self.pagina3)

        self.pagina3.setFinalPage(True)



################################   Wizard de Reparación    ######################################

        # page1 = QWizardPage()
        # page1.setTitle('Reparación')
        # page1.setSubTitle('Seleccione su tipo de ordenador y comente su problema brevemente')
        # # lineEditTipoPC = QLineEdit()
        # self.lineEditProblema = QLineEdit()
        # labelProblema = QLabel()
        # labelProblema.setText("Problema:")
        # labelTipoPC = QLabel()
        # labelTipoPC.setText("Tipo de PC:")
        # self.combopc = QComboBox()
        # self.combopc.addItem("Sobremesa")
        # self.combopc.addItem("Portátil")
        # hLayoutP1 = QHBoxLayout(page1)
        # hLayoutP1.addWidget(labelTipoPC)
        # hLayoutP1.addWidget(self.combopc)
        # # hLayoutP1.addWidget(lineEditTipoPC)
        # hLayoutP1.addWidget(labelProblema)
        # hLayoutP1.addWidget(self.lineEditProblema)
        
        # page1.registerField('problema*', self.lineEditProblema,self.lineEditProblema.text(),'textChanged')
        # self.wizard.addPage(page1)





        self.wizard = QWizard()
        

        self.wizard.setWizardStyle(QWizard.ModernStyle)

        self.wizard.setPixmap(QWizard.WatermarkPixmap,QPixmap('marcadeagua.png'))
        self.wizard.setPixmap(QWizard.LogoPixmap,QPixmap('icono.png'))
        # self.wizard.setPixmap(QWizard.BannerPixmap,QPixmap('CastaSoftIndustries.png'))

        # self.setCentralWidget(self.wizard)

        page1 = QWizardPage()
        page1.setTitle('Reparación')
        page1.setSubTitle('Seleccione su tipo de ordenador y comente su problema brevemente')
        # lineEditTipoPC = QLineEdit()
        self.lineEditProblema = QLineEdit()
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
        hLayoutP1.addWidget(self.lineEditProblema)
        
        page1.registerField('problema*', self.lineEditProblema,self.lineEditProblema.text(),'textChanged')
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
        
        self.comboDias = QComboBox()
        self.comboDias.addItem("1 Día laboral")
        self.comboDias.addItem("3 Días laborales")
        self.comboDias.addItem("5 Días laborales")
        hLayoutP3 = QHBoxLayout(page3)
        hLayoutP3.addWidget(labelDias)
        hLayoutP3.addWidget(self.comboDias)

        self.wizard.addPage(page3)

        

        page4 = QWizardPage()
        page4.setTitle('Comentarios')
        page4.setSubTitle('Indique la información adicional que quiera')
        self.textEditComentarios = QTextEdit()
        hLayoutP4 = QHBoxLayout(page4)
        hLayoutP4.addWidget(self.textEditComentarios) 


        self.wizard.addPage(page4)
        
        
        self.wizard.setWindowTitle("Asistente CastaPC")

        

        page5 = QWizardPage()
        page5.setTitle('Resumen')
        page5.setSubTitle('Confirme que estos datos son correctos, para imprimirlos pulse finish')
        labelT1 = QLabel()
        labelT1.setText("Tipo de PC: ")
        self.label1 = QLabel()
        self.label1.setText(self.combopc.currentText())
        labelT2 = QLabel()
        labelT2.setText("Problema: ")
        self.label2 = QLabel()
        self.label2.setText(self.lineEditProblema.text())
        labelT3 = QLabel()
        labelT3.setText("Piezas nuevas: ")
        self.label3 = QLabel()
        self.label3.setText(self.comboPiezas.currentText())
        labelT4 = QLabel()
        labelT4.setText("Rapidez: ")
        self.label4 = QLabel()
        self.label4.setText(self.comboDias.currentText())
        labelT5 = QLabel()
        labelT5.setText("Comentarios: ")
        self.label5 = QLabel()
        self.label5.setText(self.textEditComentarios.toPlainText())
        
        
        
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
        vLayoutP5.addLayout(hLayoutP5)
        vLayoutP5.addLayout(hLayout2P5)
        


        self.wizard.addPage(page5)

        # # next.clicked.connect(lambda:self.label1.setText(page5.field('tipoPC')))
        # next.clicked.connect(lambda:self.label2.setText(page5.field('problema')))
        # next.clicked.connect(lambda:self.label3.setText(page5.field('piezas')))
        # next.clicked.connect(lambda:self.label4.setText(page5.field('dias')))
        # next.clicked.connect(lambda:self.label5.setText(page5.field('comentarios')))

        

        page5.setFinalPage(True)

        finish = self.wizard.button(QWizard.FinishButton)

        finish.clicked.connect(self.generaPDFwizardReparacion)

        # finish = self.wizard.button(QWizard.FinishButton)
        # finish.clicked.connect(lambda:label.setText("Según su problema: "+page1.field('problema')))


        self.botonReparacion.clicked.connect(self.iniciarWizardReparacion)

        next.clicked.connect(self.actualizarDatosWizardReparacion)

        

    # Codigo db en caso de emergencia.
    def actualizarDatosWizardReparacion(self):
        self.label1.setText(str(self.combopc.currentText()))
        self.label2.setText(str(self.lineEditProblema.text()))
        self.label3.setText(str(self.comboPiezas.currentText()))
        self.label4.setText(str(self.comboDias.currentText()))
        self.label5.setText(str(self.textEditComentarios.toPlainText()))

    def actualizarDatosWizardCompra(self):
        self.labelGetNombre.setText(str(self.lineEditNombre.text()))
        self.labelGetApellido1.setText(str(self.lineEditApellido1.text()))
        self.labelGetApellido2.setText(str(self.lineEditApellido2.text()))
        self.labelGetCorreo.setText(str(self.lineEditCorreo.text()))
        self.labelGetEdad.setText(str(self.lineEditEdad.text()))
        self.labelGetTarjeta.setText(str(self.lineEditTarjeta.text()))
        self.labelGetFechaCaducidadTarjeta.setText(str(self.lineEditfechaCaducidadTarjeta.text()))
        self.labelGetCVV.setText(str(self.lineEditCVV.text()))

    def iniciarWizardReparacion(self):
        self.wizard.show()

    def iniciarWizardCompra(self):
        self.wizardCompra.show()


    def generaPDFwizardReparacion(self):
    
        outfile = "ReparacionWizard.pdf"

        template = PdfReader("PlantillaReparacionWizard.pdf", decompress=False).pages[0]
        template_obj = pagexobj(template)

        canvas = Canvas(outfile)

        xobj_name = makerl(canvas, template_obj)
        canvas.doForm(xobj_name)

        ystart = 455

        canvas.drawString(177, ystart, str(self.combopc.currentText()))

        # Ponemos la fecha de hoy
        today = datetime.today()
        canvas.drawString(455, ystart+34, today.strftime('%F'))

        # Lo ideal es partir de una posición y jugar con el tamaño de la fuente
        # En este caso, cada línea son 28 puntos
        canvas.drawString(325, ystart, str(self.lineEditProblema.text()))
        # canvas.drawString(230, ystart-28, self.data['apellidos'])

        canvas.drawString(172, ystart-(32), str(self.comboPiezas.currentText()))

        canvas.drawString(362, ystart-(32), str(self.comboDias.currentText()))

        # canvas.drawString(168, ystart-(2*32), self.data['n_perifericos'])

        # canvas.drawString(285, ystart-(2*32), self.data['perifericos'])

        # canvas.drawString(128, ystart-(3*32), self.data['direccion'])

        # canvas.drawString(472, ystart-(2*32), self.data['prueba'])

        # Sería posible establecer un límite en el número de caracteres:
        # field.setMaxLength(25)

        # Reemplazamos los saltos de línea por espacios en los comentarios
        comments = self.textEditComentarios.toPlainText().replace('\n', ' ')
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
            canvas.drawString(147, ystart-(2*32), first_line)
            # Y luego las otras cuatro
            for n, l in enumerate(lines, 1):
                canvas.drawString(80, ystart-(2*32) - (n*32), l)

        canvas.save()
        QMessageBox.information(self,"Finalizado", "Se ha generado el PDF")

    def generaPDFwizardCompra(self):
    
        outfile = "CompraWizard.pdf"

        template = PdfReader("PlantillaCompraPDF.pdf", decompress=False).pages[0]
        template_obj = pagexobj(template)

        canvas = Canvas(outfile)

        xobj_name = makerl(canvas, template_obj)
        canvas.doForm(xobj_name)

        ystart = 455

        canvas.drawString(122, ystart, str(self.lineEditNombre.text()))

        # Ponemos la fecha de hoy
        today = datetime.today()
        canvas.drawString(455, ystart, today.strftime('%F'))

        # Lo ideal es partir de una posición y jugar con el tamaño de la fuente
        # En este caso, cada línea son 28 puntos
        canvas.drawString(294, ystart, str(self.lineEditApellido1.text())+" "+str(self.lineEditApellido2.text()))
        # canvas.drawString(230, ystart-28, self.data['apellidos'])

        canvas.drawString(175, ystart-(32), str(self.lineEditCorreo.text()))

        canvas.drawString(500, ystart-(32), str(self.lineEditEdad.text()))

        canvas.drawString(190, ystart-(2*32), str(self.datosProductosTotal))

        canvas.drawString(455, ystart-(2*32), str(round(self.datosPrecioTotal,2)))

        # canvas.drawString(285, ystart-(2*32), str(self.lineEditfechaCaducidadTarjeta.text()))

        # canvas.drawString(128, ystart-(3*32), str(self.lineEditCVV.text()))

        # canvas.drawString(472, ystart-(3*32), "Python")

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

        ystart = 50

        # Dibujamos la imagen dejando 50 píxeles a la izquierda
        canvas.drawImage("graphic.png", 125, ystart, width=None,height=None,mask=None)
        canvas.save()
        QMessageBox.information(self,"Finalizado", "Se ha generado el PDF")

    def mostrarCompraPDF(self):
         # Para mostrar un PDF, es necesario habilitar los plugins. Los plugins están en https://doc.qt.io/qtforpython/PySide6/QtWebEngineCore/QWebEngineSettings.html#detailed-description
        self.webEngineWeb.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

        # Con Path guardamos la ruta relativa al documento
        self.rutaConPDF = Path("CompraWizard.pdf")
        
        # Cargamos el fichero con la ruta absoluta como uri
        # Usando http o https también se pueden cargar páginas web
        self.webEngineWeb.load(QUrl(self.rutaConPDF.absolute().as_uri()))
        # self.web.load(QUrl("https://github.com/"))

    def mostrarReparacionPDF(self):
         # Para mostrar un PDF, es necesario habilitar los plugins. Los plugins están en https://doc.qt.io/qtforpython/PySide6/QtWebEngineCore/QWebEngineSettings.html#detailed-description
        self.webEngineWeb.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

        # Con Path guardamos la ruta relativa al documento
        self.rutaConPDF2 = Path("ReparacionWizard.pdf")
        
        # Cargamos el fichero con la ruta absoluta como uri
        # Usando http o https también se pueden cargar páginas web
        self.webEngineWeb.load(QUrl(self.rutaConPDF2.absolute().as_uri()))
        # self.web.load(QUrl("https://github.com/"))

    

app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle('Casta PC')
window.show()
app.exec()