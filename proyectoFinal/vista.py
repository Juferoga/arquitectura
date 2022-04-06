from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('basic.ui', self)
        self.show()

        self.btn_reset.clicked.connect(self.resetCPU)
        self.btn_play.clicked.connect(self.startCPU)
        self.btn_debug.clicked.connect(self.startDebug)
        self.btn_load.clicked.connect(self.uploadFile)

    def resetCPU(self):
        print("funciono")
    def startCPU(self):
        print("that works")
    def startDebug(self):
        print("that works")
    def uploadFile(self):
        archivoUrl = self.txt_url.toPlainText()
        archivo = open(archivoUrl)
        contenido = archivo.read()
        cont = contenido.split('\n')
        print(cont)
        # Envio a metodo de procesado

    def setA(self):
        self.lbl_a.setText("valor")
    def setB(self):
        self.lbl_b.setText("valor")
    def setMar(self):
        self.lbl_mar.setText("valor")
    def setPC(self):
        self.lbl_pc.setText("valor")
    def setIR(self):
        self.lbl_ir.setText("valor")
    def setStatus(self):
        self.lbl_status.setText("valor")

def vista() :
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
