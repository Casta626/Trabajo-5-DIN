from PySide6.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QSpinBox


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.name = QLineEdit()
        self.apellidos = QLineEdit()
        self.tipo_ordenador = QLineEdit()
        self.marca = QLineEdit()
        self.perifericos = QLineEdit()
        self.direccion = QLineEdit()
        self.n_perifericos = QSpinBox()
        self.n_perifericos.setRange(0, 1000)
        self.comments = QTextEdit()

        self.generate_btn = QPushButton("Generar PDF")

        layout = QFormLayout()
        layout.addRow("Nombre", self.name)
        layout.addRow("Apellidos", self.apellidos)
        layout.addRow("Tipo de ordenador", self.tipo_ordenador)
        layout.addRow("Marca", self.marca)
        layout.addRow("Periféricos extra", self.perifericos)
        layout.addRow("Dirección", self.direccion)
        layout.addRow("Nº de perifericos", self.n_perifericos)

        layout.addRow("Comentarios", self.comments)
        layout.addRow(self.generate_btn)

        self.setLayout(layout)


app = QApplication([])
w = Window()
w.show()
app.exec()