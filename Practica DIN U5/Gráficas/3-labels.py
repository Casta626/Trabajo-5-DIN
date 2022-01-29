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

        # Es posible añadir títulos
        self.graphWidget.setTitle("Título del gráfico", color="b", size="30pt")

        # Y etiquetas a los ejes
        # Como font-size tiene un guión, no se puede pasar como parámetro directamente, sino usando el método **dictionary
        # Más información de **dictionary: https://stackoverflow.com/questions/21809112/what-does-tuple-and-dict-mean-in-python 
        styles = {'color':'r', 'font-size':'20px'}
        self.graphWidget.setLabel('left', 'Temperatura (°C)', **styles)
        self.graphWidget.setLabel('bottom', 'Hora (H)', **styles)

        # También admite sintaxis HTML
        #self.graphWidget.setLabel('left', "<span style=\"color:red;font-size:20px\">Temperature (°C)</span>")
        #self.graphWidget.setLabel('bottom', "<span style=\"color:red;font-size:20px\">Hour (H)</span>")

        pen = pg.mkPen(color=(255, 0, 0))
        
        self.graphWidget.plot(hour, temperature, pen=pen)

        # Y no debemos olvidarnos de las leyendas
        #self.graphWidget.addLegend()
        #self.graphWidget.plot(hour, temperature, name = "Sensor 1",  pen = pen, symbol='+', symbolSize=30, symbolBrush=('b'))


app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()