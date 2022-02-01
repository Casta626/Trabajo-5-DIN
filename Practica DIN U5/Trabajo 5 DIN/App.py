import sys
from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem, QMainWindow, QPushButton

from ui_app import Ui_MainWindow
import recursos
class MainWindow(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)



app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle('Mis Tareas')
window.show()
app.exec()