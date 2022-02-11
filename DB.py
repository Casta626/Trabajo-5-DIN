from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView,QLineEdit,QComboBox

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

                self.lineEditID = QLineEdit()
                self.lineEditProducto = QLineEdit()
                self.comboDescripcion = QComboBox()

                self.db.open()
                # Creamos una query para obtener todos los artistas de la tabla Artist
                query = QSqlQuery("SELECT descripicion FROM productos",db=self.db)
                # Recorremos el resultado de esa query agregando al comboBox el listado de artistas
                while query.next():
                     self.comboDescripcion.addItem(query.value(0))

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
                self.tableView.selectionModel().selectionChanged.connect(self.seleccion)
                # Creamos la señal: Cuando se ejecute la acción Modificar, ejecuta self.modificar
                # self.actionModificar.triggered.connect(self.modificar)
                # Creamos la señal: Cuando se ejecute la acción Insertar, ejecuta self.nueva
                # self.actionInsertar.triggered.connect(self.nueva)
                # Creamos la señal: Cuando se ejecute la acción Eliminar, ejecuta self.borrar
                # self.actionEliminar.triggered.connect(self.borrar)

                # Ponemos la fila inicial a un valor que indica que no está seleccionada ninguna fila
                self.fila = -1

        ###########################        Datos para la los Productos       #####################################

                self.queryCaja = QSqlQuery("SELECT id_producto FROM productos WHERE productos.descripcion='Caja'",db=self.db)

                while self.queryCaja.next():
                        self.idCaja=str(self.queryCaja.value(0))
                        print(self.idCaja)

                self.queryGrafica = QSqlQuery("SELECT id_producto FROM productos WHERE productos.descripcion='Grafica'",db=self.db)

                while self.queryGrafica.next():
                        self.idGrafica=str(self.queryGrafica.value(0))
                        print(self.idGrafica)

                self.queryProcesador = QSqlQuery("SELECT id_producto FROM productos WHERE productos.descripcion='Procesador'",db=self.db)

                while self.queryProcesador.next():
                        self.idProcesador=str(self.queryProcesador.value(0))
                        print(self.idProcesador)

                self.queryFA = QSqlQuery("SELECT id_producto FROM productos WHERE productos.descripcion='FA'",db=self.db)

                while self.queryFA.next():
                        self.idFA=str(self.queryFA.value(0))
                        print(self.idFA)




                
                self.queryCajaPrecio = QSqlQuery("SELECT precio FROM productos WHERE productos.precio=120.43",db=self.db)

                while self.queryCajaPrecio.next():
                        self.idCajaPrecio=self.queryCajaPrecio.value(0)
                        print(self.idCajaPrecio)


                self.queryGraficaPrecio = QSqlQuery("SELECT precio FROM productos WHERE productos.precio=999.99",db=self.db)

                while self.queryGraficaPrecio.next():
                        self.idGraficaPrecio=self.queryGraficaPrecio.value(0)
                        print(self.idGraficaPrecio)

                self.queryProcesadorPrecio = QSqlQuery("SELECT precio FROM productos WHERE productos.precio=200.83",db=self.db)

                while self.queryProcesadorPrecio.next():
                        self.idProcesadorPrecio=self.queryProcesadorPrecio.value(0)
                        print(self.idProcesadorPrecio)

                self.queryFAPrecio = QSqlQuery("SELECT precio FROM productos WHERE productos.precio=110.13",db=self.db)

                while self.queryFAPrecio.next():
                        self.idFAPrecio=self.queryFAPrecio.value(0)
                        print(self.idFAPrecio)

        #########################       Valores para la imagen de la grafica    ##############################################

                self.query = QSqlQuery("SELECT stock FROM productos",db=self.db)

        def print(self):
                while self.query.next():
                        self.indice=self.query.value(0)
                        print(self.indice)

        def seleccion(self, seleccion):
                # Recuerda que indexes almacena los índices de la selección
                if seleccion.indexes():
                # Nos quedamos con la fila del primer índice (solo se puede seleccionar una fila)
                        self.fila = seleccion.indexes()[0].row()
                        # Obtenemos los valores id, titulo y artista del modelo en esa fila
                        id = self.modelo.index(self.fila, 0).data()
                        titulo = self.modelo.index(self.fila, 1).data()
                        artista = self.modelo.index(self.fila, 2).data()
                        # Modificamos los campos del formulario para establecer esos valores
                        self.lineEditID.setText(str(id))
                        self.lineEditProducto.setText(titulo)
                        indice = self.comboDescripcion.findText(artista)
                        self.comboDescripcion.setCurrentIndex(indice)
                else:
                # Si no hay selección,  ponemos la fila inicial a un valor que indica que no está seleccionada ninguna fila
                        self.fila = -1

        def modificar(self):
                # Si es una fila válida la seleccionada
                if self.fila >= 0:
                        # Obtenemos los valores de los campos del formulario
                        id = self.lineEditID.text()
                        titulo = self.lineEditProducto.text()
                        artista = self.comboDescripcion.currentText()
                        query = QSqlQuery("SELECT descripcion FROM productos",db=self.db)
                while query.next():
                        indice=query.value(0)
                # Actualizamos los campos en el modelo
                # self.modelo.setData(self.modelo.index(self.fila, 1), id)
                # self.modelo.setData(self.modelo.index(self.fila, 1), titulo)
                # self.modelo.setData(self.modelo.index(self.fila, 2), indice)
                # Ejecutamos los cambios en el modelo
                self.modelo.submit()

        def nueva(self):
                # Guardamos en la variable nuevaFila el número de filas del modelo
                nuevaFila = self.modelo.rowCount()
                # Insertamos una nueva fila en el modelo en la posición de ese valor
                self.modelo.insertRow(nuevaFila)
                # Seleccionamos la fila nueva
                self.tableView.selectRow(nuevaFila)
                # Ponemos en blanco el texto del título en el formulario
                self.lineEditProducto.setText("")
                # Ponemos el comboBox de artistas al primero de la lista
                self.comboDescripcion.setCurrentIndex(0)
                # Establecemos en blanco los valores (título y artista) de esa nueva fila
                self.modelo.setData(self.modelo.index(nuevaFila, 1), "")
                self.modelo.setData(self.modelo.index(nuevaFila, 2), 0)
                # Ejecutamos los cambios en el modelo
                self.modelo.submit()

        def borrar(self):
                # Si es una fila válida la seleccionada
                if self.fila >= 0:
                        # Borramos la fila en el modelo
                        self.modelo.removeRow(self.fila)
                        # Actualizamos la tabla
                        self.modelo.select()
                        # Y ponemos la fila actual a -1
                        self.fila = -1
                        # Reseteamos los valores en los campos del formulario
                        self.lineEditID.setText("")
                        self.lineEditProducto.setText("")
                        self.comboDescripcion.setCurrentIndex(0)

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


