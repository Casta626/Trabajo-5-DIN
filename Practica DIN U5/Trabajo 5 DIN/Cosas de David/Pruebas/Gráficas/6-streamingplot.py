from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
import pyqtgraph as pg
import sys
from random import randint

# Para actualizar una gráfica, podemos usar self.graphWidget.clear() para limpiarla y volver a dibujarla
# Sin embargo, es mucho más eficiente usar una referencia a la línea y setData como en este ejemplo

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = list(range(100)) 
        self.y = [randint(0,100) for _ in range(100)]

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        # Guardamos una referencia a la línea
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)

        # Creamos un temporizador para actualizar cada 50ms
        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    # Método que actualiza la línea
    def update_plot_data(self):

        # Desplazamiento por el eje x
        self.x = self.x[1:]  # Eliminamos el primer elemento
        self.x.append(self.x[-1] + 1)  # Agregamos un nuevo valor uno más alto que el último

        # Añadiendo más valores al eje y
        self.y = self.y[1:]  # Eliminamos el primer elemento
        self.y.append( randint(0,100))  # Añadimos un nuevo valor aleatorio

        # Establecemos los datos actualizados a la línea
        self.data_line.setData(self.x, self.y)

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()