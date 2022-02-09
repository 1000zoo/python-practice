import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
label = QLabel("Hello")
btn = QPushButton("Ok")
btn.show()
label.show()
app.exec_()