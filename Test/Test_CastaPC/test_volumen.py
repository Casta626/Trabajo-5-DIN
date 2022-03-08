import unittest
from PySide6.QtWidgets import QApplication
from DB import DB
from Main import MainWindow


class Test (unittest.TestCase):

    def testContadorProductos(self):
        app=QApplication.instance()
        if app==None:
            app= QApplication([])
        
        window=MainWindow()
        # DB.lanzarDB(self)
        # DB.nueva(self)
        # self.contador = 0
        # window.actionInsertar.is
        





        # window.checkBoxCaja.setChecked(True)
        # window.contadorProductos()
        # self.assertEqual(window.datosProductosTotal, "1 ")
        # self.assertEqual(window.datosPrecioTotal, 120.43 )
        
if __name__ == '__main__':
    unittest.main()