from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('basic.ui', self) # Load the .ui file
        self.show() # Show the GUI

        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton') # Find the button
        self.button.clicked.connect(self.pushButton_Pressed) # Remember to pass the definition/method, not the return value!

        self.show()

    def pushButtonPressed(self):
        # This is executed when the button is pressed
        print('Reset')

        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton_2') # Find the button
        self.button.clicked.connect(self.pushButton_2Pressed) # Remember to pass the definition/method, not the return value!

        self.show()

    def pushButton_2Pressed(self):
        # This is executed when the button is pressed
        print('Play')

        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton_3') # Find the button
        self.button.clicked.connect(self.pushButton_3Pressed) # Remember to pass the definition/method, not the return value!

        self.show()

    def pushButton_3Pressed(self):
        # This is executed when the button is pressed
        print('Debug')


        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton_4') # Find the button
        self.button.clicked.connect(self.pushButton_4Pressed) # Remember to pass the definition/method, not the return value!

        self.show()

    def pushButton_4Pressed(self):
        # This is executed when the button is pressed
        print('Carga')




        self.label = self.findChild(QtWidgets.QLabel, 'lbl_2') # Find the button
      

    def Activelbl_2(self):
        # This is executed when the button is pressed
        print('lbl_2')



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
