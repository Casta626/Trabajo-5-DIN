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

        # El QPen es el equivalente al QBrush cuando dibujábamos
        # Permite asignar unas propiedades con las que después dibujar una gráfica
        pen = pg.mkPen(color=(255, 0, 0))
        
        # Qt.SolidLine, Qt.DashLine, Qt.DotLine, Qt.DashDotLine y Qt.DashDotDotLine 
        pen = pg.mkPen(color=(255, 0, 0), width=15, style=QtCore.Qt.DashLine)
        
        self.graphWidget.plot(hour, temperature, pen=pen)

        # También podemos poner marcas en los puntos
        self.graphWidget.plot(hour, temperature, symbol='+')
        # self.graphWidget.plot(hour, temperature, pen=pen, symbol='+', symbolSize=30, symbolBrush=('b'))


app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()
