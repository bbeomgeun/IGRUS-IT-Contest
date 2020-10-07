import roomAdd
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pymysql

class GUI:
    def __init__(self, ui): 
        self.window = ui
        self.privateRoom = False
        self.window.checkPassword.clicked.connect(self.checkClicked)
        self.window.roomAddClose.clicked.connect(RoomAdd.close)
        self.window.roomAddButton.clicked.connect(self.roomAddButton)

    # 방 설정을 끝낸 뒤 확인 버튼을 눌렀을 때의 이벤트 처리
    def roomAddButton(self):
        saveRn = self.window.roomname.text()
        savePro = self.window.showDirection.text()
        savePw = self.window.password.text()

        con = pymysql.connect(
            user = 'IGRUS',
            password = 'igrus1234',
            host = '13.124.126.150',
            db = 'ICBM',
            charset= 'utf8'
        )

        cursor = con.cursor()
        RoomAdd.close

        sql = "INSERT INTO table_test(roomname, profile, password) VALUES %s, %s, %s", (saveRn, 0, savePw)
        cursor.execute(sql)

        
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

def show():
    RoomAdd.show()