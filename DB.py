from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView

from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
import pyqtgraph as pg

from ui_main import Ui_MainWindow
class DB(Ui_MainWindow):
    
    def __init__(self):
        super().__init__()

    def lanzarDB(self):
        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName("DB.sqlite")

        self.db.open()
        # Creamos una query para obtener todos los artistas de la tabla Artist
        # query = QSqlQuery("SELECT Name FROM Artist",db=db)
        # Recorremos el resultado de esa query agregando al comboBox el listado de artistas
        # while query.next():
        #     self.comboBox_Artist.addItem(query.value(0))

        # Creamos un modelo relacional de SQL
        self.modelo = QSqlRelationalTableModel(db=self.db)
        # Establecemos Album como tabla del modelo
        self.modelo.setTable("productos")
        # Establecemos la relación entre el ID de los artistas y su nombre, para que se muestre este último
            
        # self.modelo.setRelation(2, QSqlRelation("Artist", "ArtistId", "Name"))
        # Hacemos el select del modelo
        self.modelo.select()
        # Renombramos las cabeceras de la tabla
        # self.modelo.setHeaderData(0, Qt.Horizontal, "Id")
        # self.modelo.setHeaderData(1, Qt.Horizontal, "Título")
        # self.modelo.setHeaderData(2, Qt.Horizontal, "Artista")
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

        self.query = QSqlQuery("SELECT stock FROM productos",db=self.db)

    def print(self):
        while self.query.next():
                self.indice=self.query.value(0)
                print(self.indice)

    def generaImgGrafica(self):
        if self.query.next():
                self.indice=self.query.value(0)
                # self.valores[] = self.query.value(0)
                print(self.indice)
        if self.query.next():
                self.indice2=self.query.value(0)
                # self.valores[] = self.query.value(0)
                print(self.indice2)
        if self.query.next():
                self.indice3=self.query.value(0)
                # self.valores[] = self.query.value(0)
                print(self.indice3)
        if self.query.next():
                self.indice4=self.query.value(0)
                # self.valores[] = self.query.value(0)
                print(self.indice4)
        else:
                print("No queda bro")

        # Generamos gráfica simple
        self.valores = [self.indice,self.indice2,self.indice3,self.indice4]
        self.plt = pg.plot(self.valores)

        self.plt.setBackground('w')

        self.plt.setTitle("Stock", color="b", size="30pt")

        styles = {'color':'r', 'font-size':'20px'}
        self.plt.setLabel('left', 'Stock de Productos', **styles)
        self.plt.setLabel('bottom', 'Diferentes Productos', **styles)

        pen = pg.mkPen(color=(255, 0, 0))

        self.plt.plot(self.valores,pen=pen)

        # Mostramos un grid en el fondo
        self.plt.showGrid(x=True, y=True)

        # Creamos una instancia de exportación con el ítem que queremos exportar
        self.exporter = pg.exporters.ImageExporter(self.plt.plotItem)

        # Establecemos los parámetros de la exportación (anchura)
        self.exporter.parameters()['width'] = 100    # (afecta a la altura de forma proporcional)

        # Elegimos el nombre del archivo en el que exportamos la gráfica como imagen
        self.exporter.export('graphic.png')

        self.outfile = "Compras.pdf"

        self.template = PdfReader("template.pdf", decompress=False).pages[0]
        self.template_obj = pagexobj(self.template)
        self.canvas = Canvas(self.outfile)

        self.xobj_name = makerl(self.canvas, self.template_obj)
        self.canvas.doForm(self.xobj_name)

        ystart = 650
        self.canvas.drawImage("graphic.png", 50, ystart, width=None,height=None,mask=None)

        self.canvas.save()
