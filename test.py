from PyQt5.QtGui import *
import sys
import os
from PyQt5.QtCore import *
# 定义：class MyView


class MyView(QGraphicsView):


        mySignal = Signal(str)
        def __init__(self):
                QGraphicsView.__init__(self)
                self.myScene = QGraphicsScene(self)       
                self.setScene(self.myScene) 
                self.pixmap = QPixmap()
       
                self.pixmap.load("temp_a.png")
                self.pixmap = self.pixmap.scaled(400, 500, Qt.KeepAspectRatio)
                self.myScene.addPixmap(self.pixmap)

# 通过mySignal把addpixmap 与UpdatePic1 链接起来。实现自动刷新图片
                self.mySignal.connect(self.UpdatePic1)
       
       

        def UpdatePic1(self, text):
                self.pixmap.load(text)
                self.pixmap = self.pixmap.scaled(400, 500, Qt.KeepAspectRatio)     
  
                self.myScene.addPixmap(self.pixmap)

if __name__ == '__main__':
   
  
        app = QApplication(sys.argv)

        mainWindow = MyView()
        mainWindow.show()
        t = threading.Thread(target=updatePic, args=(mainWindow,))
        t.start()
        sys.exit(app.exec_())
