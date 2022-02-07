from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature_1 = [30,32,34,32,33,31,29,32,35,45]
        temperature_2 = [50,35,44,22,38,32,27,38,32,44]

        self.graphWidget.setBackground('w')

        self.graphWidget.setTitle("Título de la gráfica", color="b", size="30pt")
   
        styles = {"color": "#f00", "font-size": "20px"}
        self.graphWidget.setLabel("left", "Temperatura (°C)", **styles)
        self.graphWidget.setLabel("bottom", "Hora (H)", **styles)
   
        self.graphWidget.addLegend()

        self.graphWidget.showGrid(x=True, y=True)

        self.graphWidget.setXRange(0, 10, padding=0)
        self.graphWidget.setYRange(20, 55, padding=0)

        self.plot(hour, temperature_1, "Sensor1", 'r')
        self.plot(hour, temperature_2, "Sensor2", 'b')

    # Podemos añadir más líneas simplemente añadiendo métodos plot() al mismo PlotWidget
    # Nos hacemos un método por comodidad, para usar las mismas opciones
    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=30, symbolBrush=(color))


app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()
