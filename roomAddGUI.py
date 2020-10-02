import roomAdd
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class GUI:
    def __init__(self, ui): 
        self.window = ui
        self.privateRoom = False
        self.window.checkPassword.clicked.connect(self.checkClicked)
        
    def checkClicked(self):
        if (self.privateRoom == True):
            self.privateRoom = False
            self.window.passwordInputFrame.setMinimumSize(QtCore.QSize(400, 0))
            self.window.passwordInputFrame.setMaximumSize(QtCore.QSize(400, 0))
            self.window.checkPassword.setStyleSheet("QPushButton{\n"
"    border-image: url(:/unchecked/checkbox.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border-image: url(:/unchecked/checkboxHover.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-image: url(:/unchecked/checkboxPressed.png);\n"
"}")
        elif (self.privateRoom == False):
            self.privateRoom = True
            self.window.passwordInputFrame.setMinimumSize(QtCore.QSize(400, 75))
            self.window.passwordInputFrame.setMaximumSize(QtCore.QSize(400, 16777215))
            self.window.checkPassword.setStyleSheet("QPushButton{\n"
"    border-image: url(:/checked/checkboxChecked.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border-image: url(:/checked/checkboxCheckedHover.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-image: url(:/checked/checkboxCheckedPressed.png);\n"
"}")

if __name__ != "__main__":
    app = QtWidgets.QApplication(sys.argv)
    RoomAdd = QtWidgets.QFrame()
    ui = roomAdd.Ui_roomAdd()
    ui.setupUi(RoomAdd)
    RoomAdd.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
    gui = GUI(ui)
    # sys.exit(app.exec_())

def show():
    RoomAdd.show()