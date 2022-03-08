import ctypes
from PySide6.QtCore import Property, QRect, QPropertyAnimation, QPoint, QSize, QSequentialAnimationGroup
from PySide6.QtGui import QImage, QBrush, QPainter, QWindow, QPixmap, Qt, QAction, QIcon
from PySide6.QtWidgets import QLabel, QWidget, QApplication, QSlider, QGroupBox, QMainWindow, QMenuBar, QMenu, QStatusBar, QToolBar
import sys

from ui_rebotines import Ui_MainWindow_Rebotines
 

class MainWindowRebotines(Ui_MainWindow_Rebotines, QMainWindow):

    def generaImagen(self,imgdata, imgtype, sizex): 
  
        self.sizex = 100
        self.imgtype ='jpg'
        self.img = QImage.fromData(imgdata, imgtype) 
        self.img.convertToFormat(QImage.Format_ARGB32) 
    
        self.imgsize = min(self.img.width(), self.img.height()) 
        rect = QRect( 
            (self.img.width() - self.imgsize) / 2, 
            (self.img.height() - self.imgsize) / 2, 
            self.imgsize, 
            self.imgsize, 
        ) 
        
        self.img = self.img.copy(rect) 
    
        self.out_img = QImage(self.imgsize, self.imgsize, QImage.Format_ARGB32) 
        self.out_img.fill(Qt.transparent) 
    
        self.brush = QBrush(self.img) 
    
        self.painter = QPainter(self.out_img) 
        self.painter.setBrush(self.brush) 
    
        self.painter.setPen(Qt.NoPen) 
    
        self.painter.drawEllipse(0, 0, self.imgsize, self.imgsize) 
        
        self.painter.end() 
    
        self.pr = QWindow().devicePixelRatio() 
        self.pm = QPixmap.fromImage(self.out_img) 
        self.pm.setDevicePixelRatio(self.pr) 
        sizex *= self.pr 
        self.pm = self.pm.scaled(sizex, sizex, Qt.KeepAspectRatio,  
                                Qt.SmoothTransformation) 
        return self.pm

    @property
    def imagenes(self, img, type, size):
        self.imgpath =img
        self.imgtype = type
        self.sizex = size

    @imagenes.setter
    def image(self, img, type, size):
        self.imgpath =img
        self.imgtype = type
        self.sizex = size

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Rebotes.patata(self)
        self.tamaño = 100

        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        anchura= (ancho*10)/(15*2)
        altura=(alto*10)/(15*2)
        #El valor lo multiplico por 100 y lo divido por 150 por la relación que hay en la ampliación de pantalla 
        # que trae por defecto haciendo que si la pantalla está con zoom se vea entera y si no tiene se ve con 
        # una resolucion menos.
        #La multiplicacion por 2 en las dos variables son para dividir la ventana en cuatro y así que ocupe un cuarto
        #de pantalla.

        self.setFixedWidth(anchura)
        self.setFixedHeight(altura)
        
        self.imgpath = "amsiedad.jpg"

        self.imgtype = "jpg"

        self.sizex = 25

        # self.imagenes("kk.png", "png", 56)

        print(self.imgpath)
        print(self.imgtype)
        print(self.sizex)
        
        self.imgdata = open(self.imgpath, 'rb').read() 
        
        self.pixmap = self.generaImagen(self.imgdata,self.imgtype,self.sizex) 
        
        self.bola = QLabel(self) 
        
        self.bola.setPixmap(self.pixmap) 
        
        self.bola.move(0, altura/2)

        self.horizontalSlider.setValue(600)
        

        # self.velocidad = self.horizontalSlider.value()

        self.anim = QPropertyAnimation(self.bola, b"pos")
        self.anim.setEndValue(QPoint(anchura/4, altura-74))
        # self.anim.setDuration(self.gestorVelocidad(self.velocidad))
        self.anim.setDuration(750)

        self.anim_2 = QPropertyAnimation(self.bola, b"pos")
        self.anim_2.setEndValue(QPoint(anchura-100, altura*2/5))
        # self.anim_2.setDuration(self.gestorVelocidad(self.velocidad))
        self.anim_2.setDuration(750)

        self.anim_3 = QPropertyAnimation(self.bola, b"pos")
        self.anim_3.setEndValue(QPoint(anchura*2/5, 54)) #Ahora hay que añadir 54 pixeles por la toolbar y la actionBar
        # self.anim_3.setDuration(self.gestorVelocidad(self.velocidad))
        self.anim_3.setDuration(750)

        self.anim_4 = QPropertyAnimation(self.bola, b"pos")
        self.anim_4.setEndValue(QPoint(0, altura/2))
        # self.anim_4.setDuration(self.gestorVelocidad(self.velocidad))
        self.anim_4.setDuration(750)

        self.anim_5 = QPropertyAnimation(self.bola, b"pos")
        self.anim_5.setEndValue(QPoint(200, 200))
        self.anim_5.setDuration(self.gestorVelocidad(self.velocidad))

        self.anim_group = QSequentialAnimationGroup()
        # Grupo de animación paralela
        # self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.addAnimation(self.anim_3)
        self.anim_group.addAnimation(self.anim_4)
        # self.anim_group.addAnimation(self.anim_5)
        # self.anim_group.start()

        # while True:
        
        # self.anim_group.start()
        # self.anim_group.pause()
        # self.anim_group.resume()
        # self.anim_group.stop() # Lo para por completo
        
        self.loops = 2

        self.anim_group.setLoopCount(self.loops)
        self.anim_group.start() # Solo falta ajustar la variable de velocidad para que la pille los .setDuration al momento que se cambia 

        self.horizontalSlider.setGeometry(QRect(50, altura-100, anchura-100, 16))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10000)

        self.bool = True
        self.bool2 = True

        self.actionPlay_Resume.triggered.connect(self.gestorAnimacion)
        self.actionStop.triggered.connect(self.gestorParado)
        self.actionAdvance_velocity.triggered.connect(self.aumentarVelocidad)
        self.actionRewind_velocity.triggered.connect(self.disminuirVelocidad)


        self.horizontalSlider.valueChanged.connect(self.gestorVelocidad)

        stl = """{
                margin = 0,
                bg_size = 20,
                bg_radius = 1e,
                bg color = "#1ble23",
                bg_color_hover = "#1e2229",
                handle_margin = 2,
                handle_size = 16,
                handle_radius = 8,
                handle color = "#568af2",
                handle_color_hover = "#6c99f4",
                handle_color_pressed = "#3f6fd1"
                }"""

        self.horizontalSlider.setStyleSheet("color:yellow")

    def gestorVelocidad(self, velocidad):
        print(self.horizontalSlider.value())
        self.velocidad = 10000 - velocidad
        return velocidad

    def gestorVelocidad2(self):
        self.anim_group.start()              

    def aumentarVelocidad(self):
        self.velocidad += 500
        print(self.velocidad)
    
    def disminuirVelocidad(self):
        self.velocidad -= 500
        print(self.velocidad)

    def gestorParado(self):
        if self.bool2 ==True:
            self.anim_group.stop()
            self.bool2 = False
        else:
            self.anim_group.start()
            self.bool2 = True

    
    def gestorAnimacion(self):
        if self.bool ==True:
            self.anim_group.pause()
            self.bool = False
        else:
            self.anim_group.resume()
            self.bool = True

    def getImage(self):
        return self.imgpath
    def setImage(self, img):
        self.imgpath = img
    def getImageType(self):
        return self.imgtype
    def setImageType(self, extension):
        self.imgtype = extension
    def getImageSize(self):
        return self.sizex
    def setImageSize(self, size):
        self.sizex = size

    def getLoop(self):
        return self.loops
    def setLoop(self, loop):
        self.loops = loop

    
    value1 = Property(str, getImage, setImage)
    value2 = Property(str, getImageType, setImageType)
    value3 = Property(int, getImageSize, setImageSize)
    value4 = Property(int, getLoop, setLoop)
    

# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()
# app.exec()