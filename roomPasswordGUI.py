from PyQt5 import QtCore, QtGui, QtWidgets
import roomPassword
import sys
class GUI():
    def __init__(self, ui):
        self.window = ui
        self.window.password.clicked.connect(self.clicked)
        self.window.password.released.connect(self.entered)
        self.window.passwordClose.clicked.connect(RoomPassword.close)

    def clicked(self):
        if self.window.password.text() == "암호를 입력해주세요":
            self.window.password.clear()
    
    def entered(self):
        password = self.window.password.text()
        RoomPassword.close

if __name__ != "__main__":
    app = QtWidgets.QApplication(sys.argv)
    RoomPassword = QtWidgets.QFrame()
    ui = roomPassword.Ui_roomPassword()
    ui.setupUi(RoomPassword)
    RoomPassword.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
    gui = GUI(ui)

def show():
    RoomPassword.show()