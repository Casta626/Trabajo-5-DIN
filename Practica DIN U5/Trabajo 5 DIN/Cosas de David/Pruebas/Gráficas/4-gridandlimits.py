from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore
import pyqtgraph as pg
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        self.graphWidget.setBackground('w')

        self.graphWidget.setTitle("Título del gráfico", color="b", size="30pt")

        styles = {'color':'r', 'font-size':'20px'}
        self.graphWidget.setLabel('left', 'Temperatura (°C)', **styles)
        self.graphWidget.setLabel('bottom', 'Hora (H)', **styles)

        pen = pg.mkPen(color=(255, 0, 0))

        # Mostramos un grid en el fondo
        self.graphWidget.showGrid(x=True, y=True)

        # Podemos establecer un mínimo y un máximo para los ejes (para mostrar esa parte en concreto)
        self.graphWidget.setXRange(5, 20, padding=0)
        self.graphWidget.setYRange(30, 40, padding=0)
        
        self.graphWidget.plot(hour, temperature, pen=pen)

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()