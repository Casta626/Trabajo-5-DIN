import unittest
from PySide6.QtWidgets import QApplication
from Main import MainWindow


class Test (unittest.TestCase):

    def testContadorProductos(self):
        app=QApplication.instance()
        if app==None:
            app= QApplication([])
        
        window=MainWindow()
        window.checkBoxCaja.setChecked(True)
        window.contadorProductos()
        self.assertEqual(window.datosProductosTotal, "1 ")
        self.assertEqual(window.datosPrecioTotal, 120.43 )
        

    # def testImage(self):
    #     app=QApplication.instance()
    #     if app==None:
    #         app= QApplication([])
        
    #     window=MainWindow()
    #     window.setImage("cocos.png") 
    #     self.assertEqual(window.getImage(), "cocos.png")

    #     window.setImageType("png")
    #     self.assertEqual(window.getImageType(), "png")

    #     window.setImageSize(24)
    #     self.assertEqual(window.getImageSize(), 24)

    # def testLoop(self):
    #     app=QApplication.instance()
    #     if app==None:
    #         app= QApplication([])
        
        # window=MainWindow()
        # window.setLoop(4)
        # self.assertEqual(window.getLoop(), 4)
        
if __name__ == '__main__':
    unittest.main()


    
    