from PySide6 import QtWidgets
from rebotines import MainWindowRebotines

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        mainToggle = MainWindowRebotines()
        mainToggle.setLoop(2)
        mainToggle.setImage("amsiedad.png")
        mainToggle.setImageType("png")
        mainToggle.setImageSize(120)
        self.setCentralWidget(mainToggle)
        
        

app = QtWidgets.QApplication([])
w = Window()
w.show()
app.exec()