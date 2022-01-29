# reportlab permite la creación de PDF usando texto y primitivas de dibujo
from reportlab.pdfgen.canvas import Canvas
# pdfrw permite leer y extraer páginas de archivos PDF
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

# Nombre del PDF resultante
outfile = "result.pdf"

# Guardamos en template la primera página del PDF que usamos de plantilla
template = PdfReader("template.pdf", decompress=False).pages[0]
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