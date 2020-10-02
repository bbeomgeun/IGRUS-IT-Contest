from PyQt5 import QtCore, QtGui, QtWidgets
import roomSetting
import sys
class GUI():
    def __init__(self, ui):
        self.window = ui



if __name__ != "__main__":
    app = QtWidgets.QApplication(sys.argv)
    RoomSetting = QtWidgets.QFrame()
    ui = roomSetting.Ui_roomSetting()
    ui.setupUi(RoomSetting)
    RoomSetting.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
    gui = GUI(ui)

def show():
    RoomSetting.show()
