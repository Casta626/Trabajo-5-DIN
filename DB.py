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
                self.db.setDatabaseName("sqlitePrueba.sqlite")

                self.db.open()

                # Deshabilitamos la edición del cuadro de texto del ID
                self.lineEditIDDB.setEnabled(False)

                # Creamos una query para obtener todos los artistas de la tabla Artist
                self.queryCombo = QSqlQuery("SELECT DISTINCT  descripcion FROM productos",db=self.db)
                # Recorremos el resultado de esa query agregando al comboBox el listado de artistas
                while self.queryCombo.next():
                     self.comboBoxDescripcionDB.addItem(self.queryCombo.value(0))
                     print(self.comboBoxDescripcionDB)

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
                self.tablaDB.setModel(self.modelo)
                # Ajustamos el tamaño de las columnas al contenido
                self.tablaDB.resizeColumnsToContents()

                # Deshabilitamos la edición directa de la tabla
                self.tablaDB.setEditTriggers(QAbstractItemView.NoEditTriggers)
                # Establecemos que se seleccionen filas completas en lugar de celdas individuales
                self.tablaDB.setSelectionMode(QAbstractItemView.SingleSelection)
                self.tablaDB.setSelectionBehavior(QAbstractItemView.SelectRows)

                # Creamos la señal: Cuando cambie la seleccion, ejecuta self.seleccion
                self.tablaDB.selectionModel().selectionChanged.connect(self.seleccion)
                # Creamos la señal: Cuando se ejecute la acción Modificar, ejecuta self.modificar
                self.actionModificar.triggered.connect(self.modificar)
                # Creamos la señal: Cuando se ejecute la acción Insertar, ejecuta self.nueva
                self.actionInsertar.triggered.connect(self.nueva)
                # Creamos la señal: Cuando se ejecute la acción Eliminar, ejecuta self.borrar
                self.actionEliminar.triggered.connect(self.borrar)

                # Ponemos la fila inicial a un valor que indica que no está seleccionada ninguna fila
                self.fila = -1

        ###########################        Datos para la los Productos       #####################################

                self.queryCaja = QSqlQuery("SELECT id_producto FROM productos WHERE productos.id_producto=1",db=self.db)

                while self.queryCaja.next():
                        self.idCaja=str(self.queryCaja.value(0))
                        print(self.idCaja)

                self.queryGrafica = QSqlQuery("SELECT id_producto FROM productos WHERE productos.id_producto=2",db=self.db)

                while self.queryGrafica.next():
                        self.idGrafica=str(self.queryGrafica.value(0))
                        print(self.idGrafica)

                self.queryProcesador = QSqlQuery("SELECT id_producto FROM productos WHERE productos.id_producto=3",db=self.db)

                while self.queryProcesador.next():
                        self.idProcesador=str(self.queryProcesador.value(0))
                        print(self.idProcesador)

                self.queryFA = QSqlQuery("SELECT id_producto FROM productos WHERE productos.id_producto=4",db=self.db)

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

                self.query = QSqlQuery("SELECT  stock FROM productos",db=self.db)

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
                        producto = self.modelo.index(self.fila, 1).data()
                        descripcion = self.modelo.index(self.fila, 2).data()
                        precio = self.modelo.index(self.fila, 3).data()
                        stock = self.modelo.index(self.fila, 4).data()
                        # Modificamos los campos del formulario para establecer esos valores
                        self.lineEditIDDB.setText(str(id))
                        self.lineEditProductoDB.setText(producto)
                        valorModificar = self.comboBoxDescripcionDB.findText(descripcion)
                        self.comboBoxDescripcionDB.setCurrentIndex(valorModificar)
                        self.lineEditPrecioDB.setText(str(precio))
                        self.lineEditStockDB.setText(str(stock))
                else:
                # Si no hay selección,  ponemos la fila inicial a un valor que indica que no está seleccionada ninguna fila
                        self.fila = -1

        def modificar(self):
                # Si es una fila válida la seleccionada
                if self.fila >= 0:
                        # Obtenemos los valores de los campos del formulario
                        id = self.lineEditIDDB.text()
                        producto = self.lineEditProductoDB.text()
                        descripcion = self.comboBoxDescripcionDB.currentText()
                        query = QSqlQuery("SELECT descripcion FROM productos WHERE descripcion='"+descripcion+"'",db=self.db)
                        precio = self.lineEditPrecioDB.text()
                        stock = self.lineEditStockDB.text()
                        while query.next():
                                self.valorModificar=query.value(0)
                                print(self.valorModificar)
                        # Actualizamos los campos en el modelo
                        self.modelo.setData(self.modelo.index(self.fila, 1), id)
                        self.modelo.setData(self.modelo.index(self.fila, 1), producto)
                        self.modelo.setData(self.modelo.index(self.fila, 2), self.valorModificar)
                        self.modelo.setData(self.modelo.index(self.fila, 3), precio)
                        self.modelo.setData(self.modelo.index(self.fila, 4), stock)
                        # Ejecutamos los cambios en el modelo
                        self.modelo.submit()

        def nueva(self):
                # Guardamos en la variable nuevaFila el número de filas del modelo
                nuevaFila = self.modelo.rowCount()
                # Insertamos una nueva fila en el modelo en la posición de ese valor
                self.modelo.insertRow(nuevaFila)
                # Seleccionamos la fila nueva
                self.tablaDB.selectRow(nuevaFila)
                # Ponemos en blanco el texto del título en el formulario
                self.lineEditProductoDB.setText("")
                # Ponemos el comboBox de artistas al primero de la lista
                self.comboBoxDescripcionDB.setCurrentIndex(0)
                # Establecemos en blanco los valores (título y artista) de esa nueva fila
                self.modelo.setData(self.modelo.index(nuevaFila, 1), "")
                self.modelo.setData(self.modelo.index(nuevaFila, 2), "")
                self.modelo.setData(self.modelo.index(nuevaFila, 3), "")
                self.modelo.setData(self.modelo.index(nuevaFila, 4), "")
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
                        self.lineEditIDDB.setText("")
                        self.lineEditProductoDB.setText("")
                        self.comboBoxDescripcionDB.setCurrentIndex("")
                        self.lineEditPrecioDB.setText("")
                        self.lineEditStockDB.setText("")


        def generaImgGrafica(self):

                # arrayStock = []
                # while self.query.next():
                #         arrayStock.append(self.query.value(0))
                #         # self.valores[] = self.query.value(0)
                #         print(arrayStock)
                
                # # Generamos gráfica simple
                # # self.valores = [self.arrayStock,self.indice2,self.indice3,self.indice4]
                # self.plt = pg.plot(arrayStock)

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
                self.exporter.parameters()['width'] = 350    # (afecta a la altura de forma proporcional)

                # Elegimos el nombre del archivo en el que exportamos la gráfica como imagen
                self.exporter.export('graphic.png')

                self.outfile = "Compras.pdf"

                self.template = PdfReader("PlantillaReparacionWizard.pdf", decompress=False).pages[0]
                self.template_obj = pagexobj(self.template)
                self.canvas = Canvas(self.outfile)

                self.xobj_name = makerl(self.canvas, self.template_obj)
                self.canvas.doForm(self.xobj_name)

                ystart = 650
                self.canvas.drawImage("graphic.png", 50, ystart, width=None,height=None,mask=None)

                self.canvas.save()


