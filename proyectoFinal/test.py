from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('basic.ui', self)
        self.show()

def vista() :
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
