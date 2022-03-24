from curses import window
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Creando la ventana
def ventana():
    # Creando la app :)
    app = QApplication(sys.argv)
    win = QWidget()
    lbl1 = QLabel(win)
    lbl1.setText("haha por lo menos una etiqueta crack")
    win.setGeometry(100,100,200,50)
    lbl1.move(50,20)
    win.setWindowTitle("Hola mundo")
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    ventana()
