import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 300, 400) #(내 모니터 내의 좌표)ax, ay, (윈도우 창의 크기)aw, ah
        self.setWindowTitle("1000zoo")
        self.setWindowIcon(QIcon("icon/myIcon1"))
        
        btn = QPushButton("OK", self)
        btn.move(150,200)
        label = QLabel("Hello", self)
        
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()