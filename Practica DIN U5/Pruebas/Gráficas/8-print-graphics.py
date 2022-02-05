from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
import pyqtgraph as pg
import pyqtgraph.exporters

# Generamos gráfica simple
plt = pg.plot([1,5,2,4,3])

# Creamos una instancia de exportación con el ítem que queremos exportar
exporter = pg.exporters.ImageExporter(plt.plotItem)

# Establecemos los parámetros de la exportación (anchura)
exporter.parameters()['width'] = 10000   # (afecta a la altura de forma proporcional)

# Elegimos el nombre del archivo en el que exportamos la gráfica como imagen
exporter.export('graphic.png')

outfile = "result.pdf"

template = PdfReader("template2.pdf", decompress=False).pages[0]
template_obj = pagexobj(template)
canvas = Canvas(outfile)

xobj_name = makerl(canvas, template_obj)
canvas.doForm(xobj_name)

ystart = 650
canvas.drawImage("graphic.png", 50, ystart, width=None,height=None,mask=None)

canvas.save()