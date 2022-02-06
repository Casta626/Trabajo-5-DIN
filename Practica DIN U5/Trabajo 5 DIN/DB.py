from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView
from ui_main import Ui_MainWindow
class DB(Ui_MainWindow):
    
    def __init__(self):
        super().__init__()

    def db(self):
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("DB.sqlite")

        db.open()
        # Creamos una query para obtener todos los artistas de la tabla Artist
        # query = QSqlQuery("SELECT Name FROM Artist",db=db)
        # Recorremos el resultado de esa query agregando al comboBox el listado de artistas
        # while query.next():
        #     self.comboBox_Artist.addItem(query.value(0))

        # Creamos un modelo relacional de SQL
        self.modelo = QSqlRelationalTableModel(db=db)
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

        self.query = QSqlQuery("SELECT stock FROM productos",db=db)
        self.q1 = self.query.value(0) 
        self.q2 = self.query.value(1) 
        self.q3 = self.query.value(2)
        self.q4 = self.query.value(3)

    def print(self):
        while self.query.next():
                indice=self.query.value(0)
                print(indice)