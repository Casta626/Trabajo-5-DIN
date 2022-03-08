import unittest
from PySide6.QtWidgets import QApplication
from rebotines import MainWindowRebotines


class Test (unittest.TestCase):

    def testSlider(self):
        app=QApplication.instance()
        if app==None:
            app= QApplication([])
        
        window=MainWindowRebotines()
        window.horizontalSlider.setValue(700)
        self.assertEqual(window.horizontalSlider.value(), 700)

    def testImage(self):
        app=QApplication.instance()
        if app==None:
            app= QApplication([])
        
        window=MainWindowRebotines()
        window.setImage("cocos.png") 
        self.assertEqual(window.getImage(), "cocos.png")

        window.setImageType("png")
        self.assertEqual(window.getImageType(), "png")

        window.setImageSize(24)
        self.assertEqual(window.getImageSize(), 24)

    def testLoop(self):
        app=QApplication.instance()
        if app==None:
            app= QApplication([])
        
        window=MainWindowRebotines()
        window.setLoop(4)
        self.assertEqual(window.getLoop(), 4)
        
if __name__ == '__main__':
    unittest.main()


    
    