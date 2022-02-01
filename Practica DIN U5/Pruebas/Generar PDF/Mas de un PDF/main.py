from PySide6.QtWidgets import QFileDialog, QMessageBox, QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QSpinBox
from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
import os
import csv
import textwrap
from datetime import datetime
# Librería que trabaja con el sistema operativo
# En este caso, para obtener la ruta del fichero
import os
# Librería para leer y manipular archivos CSV
import csv

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.sourcefile = QLineEdit()
        self.sourcefile.setDisabled(True)

        self.file_select = QPushButton("Selecciona el CSV...")
        self.file_select.pressed.connect(self.choose_csv_file)

        self.generate_btn = QPushButton("Generar archivos PDF")
        self.generate_btn.pressed.connect(self.generate)

        layout = QFormLayout()
        layout.addRow(self.sourcefile, self.file_select)
        layout.addRow(self.generate_btn)

        self.setLayout(layout)
    # Diálogo para seleccionar un archivo CSV
    def choose_csv_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Selecciona un fichero", filter="CSV files (*.csv)")
        if filename:
            self.sourcefile.setText(filename)

    def generate(self):
        # Si no hay archivo seleccionado, ignorar
        if not self.sourcefile.text():
            return 

        self.generate_btn.setDisabled(True)

        # Obtenemos los datos del archivo
        self.data = {
            'sourcefile': self.sourcefile.text(),
        }
        # Obtenemos el nombre del archivo
        filename, _ = os.path.splitext(self.data['sourcefile'])
        # Y la carpeta en la que se encuentra
        folder = os.path.dirname(self.data['sourcefile'])

        template = PdfReader("template2.pdf", decompress=False).pages[0]
        template_obj = pagexobj(template)

        # Abrimos el archivo CSV
        with open(self.data['sourcefile'], 'r', newline='') as f:
            reader = csv.DictReader(f)

            # Por cada elemento y línea (por cada archivo PDF a generar)
            for n, row in enumerate(reader, 1):
                # Creamos el nombre del archivo
                fn = f'{filename}-{n}.pdf'
                # Indicamos la carpeta donde se guardará
                outfile = os.path.join(folder, fn)

                # Rellenamos el PDF partiendo de la plantilla
                canvas = Canvas(outfile)

                xobj_name = makerl(canvas, template_obj)
                canvas.doForm(xobj_name)

                # ystart = 443

                # canvas.drawString(170, ystart, row.get('name', ''))

                # today = datetime.today()
                # canvas.drawString(410, ystart, today.strftime('%F'))

                # canvas.drawString(230, ystart-28, row.get('program_type', ''))

                # canvas.drawString(175, ystart-(2*28), row.get('product_code', ''))

                # canvas.drawString(315, ystart-(2*28), row.get('customer', ''))

                # canvas.drawString(145, ystart-(3*28), row.get('vendor', ''))

                # ystart = 250

                # canvas.drawString(210, ystart, "Python")

                # canvas.drawString(430, ystart, row.get('n_errors', ''))

                ystart = 455

                canvas.drawString(122, ystart, row.get('nombre', ''))

                today = datetime.today()
                canvas.drawString(455, ystart, today.strftime('%F'))

                canvas.drawString(294, ystart, row.get('apellidos', ''))

                canvas.drawString(175, ystart-32, row.get('tipo_ordenador', ''))

                canvas.drawString(290, ystart-32, row.get('marca', ''))

                canvas.drawString(423, ystart-32, row.get('precio', ''))

                canvas.drawString(168, ystart-(2*32), row.get('n_perifericos', ''))

                canvas.drawString(285, ystart-(2*32), row.get('perifericos', ''))

                canvas.drawString(128, ystart-(3*32), row.get('direccion', ''))

                canvas.drawString(472, ystart-(3*32), "Python")

                comments = row.get('comments', '').replace('\n', ' ')
                if comments:
                    lines = textwrap.wrap(comments, width=65) # 45
                    first_line = lines[0]
                    remainder = ' '.join(lines[1:])

                    lines = textwrap.wrap(remainder, 75) # 55
                    lines = lines[:4]  # max lines, not including the first.

                    canvas.drawString(155, ystart-(4*32), first_line)
                    for n, l in enumerate(lines, 1):
                        canvas.drawString(80, ystart-(4*32) - (n*32), l)

                canvas.save()
        QMessageBox.information(self, "Finalizado", "Se han generado los archivos PDF")

app = QApplication([])
w = Window()
w.show()
app.exec()