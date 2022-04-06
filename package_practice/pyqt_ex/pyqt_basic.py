import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
label = QLabel("Hello")
label.show()
# btn = QPushButton("Ok")
# btn.show()
app.exec_()