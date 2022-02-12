
from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
import pyqtgraph as pg
import pyqtgraph.exporters

from pruebaDefinitiva2 import Ui_MainWindow
from DB import DB

class Graficas(DB,Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Poner lo común

    # def generaImgGrafica(self):
    #     DB.lanzarDB(self)
    #     if self.query.next():
    #             self.indice=self.query.value(0)
    #             # self.valores[] = self.query.value(0)
    #             print(self.indice)
    #     if self.query.next():
    #             self.indice2=self.query.value(0)
    #             # self.valores[] = self.query.value(0)
    #             print(self.indice2)
    #     if self.query.next():
    #             self.indice3=self.query.value(0)
    #             # self.valores[] = self.query.value(0)
    #             print(self.indice3)
    #     if self.query.next():
    #             self.indice4=self.query.value(0)
    #             # self.valores[] = self.query.value(0)
    #             print(self.indice4)
    #     else:
    #             print("No queda bro")

    #     # Generamos gráfica simple
    #     self.valores = [self.indice,self.indice2,self.indice3,self.indice4]
    #     self.plt = pg.plot(self.valores)

    #     self.plt.setBackground('w')

    #     self.plt.setTitle("Stock", color="b", size="30pt")

    #     styles = {'color':'r', 'font-size':'20px'}
    #     self.plt.setLabel('left', 'Stock de Productos', **styles)
    #     self.plt.setLabel('bottom', 'Diferentes Productos', **styles)

    #     pen = pg.mkPen(color=(255, 0, 0))

    #     self.plt.plot(self.valores,pen=pen)

    #     # Mostramos un grid en el fondo
    #     self.plt.showGrid(x=True, y=True)

    #     # Creamos una instancia de exportación con el ítem que queremos exportar
    #     self.exporter = pg.exporters.ImageExporter(self.plt.plotItem)

    #     # Establecemos los parámetros de la exportación (anchura)
    #     self.exporter.parameters()['width'] = 100    # (afecta a la altura de forma proporcional)

    #     # Elegimos el nombre del archivo en el que exportamos la gráfica como imagen
    #     self.exporter.export('graphic.png')

    #     self.outfile = "result.pdf"

    #     self.template = PdfReader("template.pdf", decompress=False).pages[0]
    #     self.template_obj = pagexobj(self.template)
    #     self.canvas = Canvas(self.outfile)

    #     self.xobj_name = makerl(self.canvas, self.template_obj)
    #     self.canvas.doForm(self.xobj_name)

    #     ystart = 650
    #     self.canvas.drawImage("graphic.png", 50, ystart, width=None,height=None,mask=None)

    #     self.canvas.save()

    def generaGrafica(self):
        # Nombre del PDF resultante
        outfile = "result.pdf"

        # Guardamos en template la primera página del PDF que usamos de plantilla
        template = PdfReader("template2.pdf", decompress=False).pages[0]
        # La convertimos en un Form XObject
        # Esto permite incluir de forma limpia un fragmento de un archivo PDF (en este caso, la página completa) en otro PDF
        template_obj = pagexobj(template)

        # Creamos un canvas de reportlab para dibujar en el PDF resultante
        canvas = Canvas(outfile)

        # Generamos un objeto canvas con la plantilla
        xobj_name = makerl(canvas, template_obj)
        # Y lo añadimos al canvas creado para el resultado
        canvas.doForm(xobj_name)

        # Elegimos la altura de la imagen
        ystart = 650

        # Dibujamos la imagen dejando 50 píxeles a la izquierda
        canvas.drawImage("image.png", 50, ystart, width=None,height=None,mask=None)

        # Guardamos el canvas
        canvas.save()