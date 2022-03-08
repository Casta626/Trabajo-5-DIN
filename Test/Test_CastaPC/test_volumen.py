import unittest
from PySide6.QtWidgets import QApplication
from Main import MainWindow


class Test (unittest.TestCase):

    def testContadorProductos(self):
        app=QApplication.instance()
        if app==None:
            app= QApplication([])
        
        window=MainWindow()
        self.texto = "a"
        window.checkBoxCaja.setChecked(True)
        window.contadorProductos()
        self.assertEqual(window.datosProductosTotal, "1 ")
        self.assertEqual(window.datosPrecioTotal, 120.43 )
        
if __name__ == '__main__':
    unittest.main()