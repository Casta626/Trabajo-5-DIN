from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import sys

from pyqtgraph.Qt import QtGui

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Todas las gráficas son un widget PlotWidget
        # Proporciona un canvas en el que dibujar cualquier gráfica
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        # Representamos los puntos de hora y temperatura
        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        # Podemos cambiar el fondo, con muchas formas de definir el color
        # self.graphWidget.setBackground('w')
        # self.graphWidget.setBackground('#bbccaa')
        # self.graphWidget.setBackground((100,50,255,25)) #RGBA
        self.graphWidget.setBackground(QtGui.QColor(100,50,254,25))

        # Y los dibujamos (x,y)
        self.graphWidget.plot(hour, temperature)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()