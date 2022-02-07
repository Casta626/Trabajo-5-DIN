import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractItemView
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel
from PySide6.QtCore import Qt
from design_David import Ui_MainWindow

# Realizamos la carga y apertura de la base de datos
db = QSqlDatabase("QSQLITE")
db.setDatabaseName("chinook.sqlite")

db.open()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        # Cargamos la UI
        self.setupUi(self)

        # Deshabilitamos la edición del cuadro de texto del ID
        self.lineEdit_ID.setEnabled(False)

        # Creamos una query para obtener todos los artistas de la tabla Artist
        query = QSqlQuery("SELECT Name FROM Artist",db=db)
        # Recorremos el resultado de esa query agregando al comboBox el listado de artistas
        while query.next():
            self.comboBox_Artist.addItem(query.value(0))

        # Creamos un modelo relacional de SQL
        self.modelo = QSqlRelationalTableModel(db=db)
        # Establecemos Album como tabla del modelo
        self.modelo.setTable("Album")
        # Establecemos la relación entre el ID de los artistas y su nombre, para que se muestre este último
        self.modelo.setRelation(2, QSqlRelation("Artist", "ArtistId", "Name"))
        # Hacemos el select del modelo
        self.modelo.select()
        # Renombramos las cabeceras de la tabla
        self.modelo.setHeaderData(0, Qt.Horizontal, "Id")
        self.modelo.setHeaderData(1, Qt.Horizontal, "Título")
        self.modelo.setHeaderData(2, Qt.Horizontal, "Artista")

        # Establecemos el modelo en el tableView
        self.tabla.setModel(self.modelo)
        # Ajustamos el tamaño de las columnas al contenido
        self.tabla.resizeColumnsToContents()

        # Deshabilitamos la edición directa de la tabla
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Establecemos que se seleccionen filas completas en lugar de celdas individuales
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Creamos la señal: Cuando cambie la seleccion, ejecuta self.seleccion
        self.tabla.selectionModel().selectionChanged.connect(self.seleccion)
        # Creamos la señal: Cuando se ejecute la acción Modificar, ejecuta self.modificar
        self.actionModificar.triggered.connect(self.modificar)
        # Creamos la señal: Cuando se ejecute la acción Insertar, ejecuta self.nueva
        self.actionInsertar.triggered.connect(self.nueva)
        # Creamos la señal: Cuando se ejecute la acción Eliminar, ejecuta self.borrar
        self.actionEliminar.triggered.connect(self.borrar)

        # Ponemos la fila inicial a un valor que indica que no está seleccionada ninguna fila
        self.fila = -1

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
            self.lineEdit_ID.setText(str(id))
            self.lineEdit_Title.setText(titulo)
            indice = self.comboBox_Artist.findText(artista)
            self.comboBox_Artist.setCurrentIndex(indice)
        else:
            # Si no hay selección,  ponemos la fila inicial a un valor que indica que no está seleccionada ninguna fila
            self.fila = -1

    def modificar(self):
        # Si es una fila válida la seleccionada
        if self.fila >= 0:
            # Obtenemos los valores de los campos del formulario
            id = self.lineEdit_ID.text()
            titulo = self.lineEdit_Title.text()
            artista = self.comboBox_Artist.currentText()
            query = QSqlQuery("SELECT ArtistID FROM Artist WHERE Name='"+artista+"'",db=db)
            while query.next():
                indice=query.value(0)
            # Actualizamos los campos en el modelo
            self.modelo.setData(self.modelo.index(self.fila, 1), id)
            self.modelo.setData(self.modelo.index(self.fila, 1), titulo)
            self.modelo.setData(self.modelo.index(self.fila, 2), indice)
            # Ejecutamos los cambios en el modelo
            self.modelo.submit()

    def nueva(self):
        # Guardamos en la variable nuevaFila el número de filas del modelo
        nuevaFila = self.modelo.rowCount()
        # Insertamos una nueva fila en el modelo en la posición de ese valor
        self.modelo.insertRow(nuevaFila)
        # Seleccionamos la fila nueva
        self.tabla.selectRow(nuevaFila)
        # Ponemos en blanco el texto del título en el formulario
        self.lineEdit_Title.setText("")
        # Ponemos el comboBox de artistas al primero de la lista
        self.comboBox_Artist.setCurrentIndex(0)
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
            self.lineEdit_ID.setText("")
            self.lineEdit_Title.setText("")
            self.comboBox_Artist.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
