from PySide6.QtWidgets import QMessageBox, QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QSpinBox
from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
# Para ajustar el texto de los comentarios
import textwrap
# Para poner la fecha de hoy
from datetime import datetime

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.nombre = QLineEdit()
        self.apellidos = QLineEdit()
        self.tipo_ordenador = QLineEdit()
        self.marca = QLineEdit()
        self.precio = QLineEdit()
        self.n_perifericos = QSpinBox()
        self.n_perifericos.setRange(0, 1000)
        self.perifericos = QLineEdit()
        self.direccion = QLineEdit()
        self.comments = QTextEdit()

        self.generate_btn = QPushButton("Generar PDF")

        layout = QFormLayout()
        layout.addRow("Nombre", self.nombre)
        layout.addRow("Apellidos", self.apellidos)
        layout.addRow("Tipo de ordenador", self.tipo_ordenador)
        layout.addRow("Marca", self.marca)
        layout.addRow("Precio", self.precio)
        layout.addRow("Nº de perifericos", self.n_perifericos)
        layout.addRow("Periféricos extra", self.perifericos)
        layout.addRow("Dirección", self.direccion)
        

        layout.addRow("Comentarios", self.comments)
        layout.addRow(self.generate_btn)

        self.setLayout(layout)
        # Conectamos el botón con el método generate
        self.generate_btn.pressed.connect(self.generate)

    def generate(self):
        self.generate_btn.setDisabled(True)
        # Creamos un diccionario con los datos (opcional)
        self.data = {
            'nombre': self.nombre.text(),
            'apellidos': self.apellidos.text(),
            'tipo_ordenador': self.tipo_ordenador.text(),
            'marca': self.marca.text(),
            'precio': self.precio.text(),
            'direccion': self.direccion.text(),
            'perifericos': self.perifericos.text(),
            'n_perifericos': str(self.n_perifericos.value()),
            'comments': self.comments.toPlainText()
        }
        outfile = "result2.pdf"

        template = PdfReader("template2.pdf", decompress=False).pages[0]
        template_obj = pagexobj(template)

        canvas = Canvas(outfile)

        xobj_name = makerl(canvas, template_obj)
        canvas.doForm(xobj_name)

        ystart = 455

        canvas.drawString(122, ystart, self.data['nombre'])

        # Ponemos la fecha de hoy
        today = datetime.today()
        canvas.drawString(455, ystart, today.strftime('%F'))

        # Lo ideal es partir de una posición y jugar con el tamaño de la fuente
        # En este caso, cada línea son 28 puntos
        canvas.drawString(294, ystart, self.data['apellidos'])
        # canvas.drawString(230, ystart-28, self.data['apellidos'])

        canvas.drawString(175, ystart-(32), self.data['tipo_ordenador'])

        canvas.drawString(290, ystart-(32), self.data['marca'])

        canvas.drawString(423, ystart-(32), self.data['precio'])

        canvas.drawString(168, ystart-(2*32), self.data['n_perifericos'])

        canvas.drawString(285, ystart-(2*32), self.data['perifericos'])

        canvas.drawString(128, ystart-(3*32), self.data['direccion'])

        canvas.drawString(472, ystart-(3*32), "Python")

       

        # Sería posible establecer un límite en el número de caracteres:
        # field.setMaxLength(25)

        # Reemplazamos los saltos de línea por espacios en los comentarios
        comments = self.data['comments'].replace('\n', ' ')
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

app = QApplication([])
w = Window()
w.show()
app.exec()