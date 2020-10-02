from PyQt5 import QtCore, QtGui, QtWidgets
import roomPassword
import sys
class GUI():
    def __init__(self, ui):
        self.window = ui



if __name__ != "__main__":
    app = QtWidgets.QApplication(sys.argv)
    RoomPassword = QtWidgets.QFrame()
    ui = roomPassword.Ui_roomPassword()
    ui.setupUi(RoomPassword)
    RoomPassword.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
    gui = GUI(roomPassword)
    # sys.exit(app.exec_())

def show():
    RoomPassword.show()