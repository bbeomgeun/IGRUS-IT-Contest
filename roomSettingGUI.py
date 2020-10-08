from PyQt5 import QtCore, QtGui, QtWidgets
import roomSetting
import sys
import pymysql

class GUI():
    def __init__(self, ui):
        self.window = ui
        self.privateRoom = False
        self.window.checkPassword.clicked.connect(self.checkClicked)
        self.window.roomSettingButton.clicked.connect(self.settingroom)
        self.window.findFile.clicked.connect(self.getFile)
        self.window.roomSettingClose.clicked.connect(RoomSetting.close)
        self.inputFilePath = ""
        
    def firstSet(self):
        cursor.execute("SELECT * FROM room WHERE idx = %s", (roomnum, ))
        data = cursor.fetchall()[0]
        self.window.roomname.setText(data[1])
        if data[2] == 1:
            self.window.password.setText(data[3])
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

    def settingroom(self):
        cursor.execute("SELECT * FROM room WHERE idx = %s", (roomnum, ))
        data = cursor.fetchall()[0]
        if self.window.roomname.text() != data[1]:
            cursor.execute("UPDATE member SET title = %s WHERE idx = %s", (self.window.roomname.text(), roomnum))
            con.commit()
            win.chatRoomTitle.setText(self.window.roomname.text())
        if self.window.password.text() != data[3]:
            cursor.execute("UPDATE member SET title = %s WHERE idx = %s", (self.window.password.text(), roomnum))
            con.commit()
            con.close()
        RoomSetting.close

    def getFile(self):
        self.filePath = QtWidgets.QFileDialog.getOpenFileName()
        self.inputFilePath = self.filePath[0]
        self.realName = self.filePath[0].split('/')
        self.window.showDirection.setText(self.realName[len(self.realName) - 1])

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
    global cursor, con
    con = pymysql.connect(
    user = 'IGRUS',
    password = 'igrus1234',
    host = '13.124.126.150',
    db = 'ICBM',
    charset= 'utf8'
    )
    cursor = con.cursor()
    app = QtWidgets.QApplication(sys.argv)
    RoomSetting = QtWidgets.QFrame()
    ui = roomSetting.Ui_roomSetting()
    ui.setupUi(RoomSetting)
    RoomSetting.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
    gui = GUI(ui)

def show(window):

    RoomSetting.show()
    roomtitle = str(window.chatRoomTitle.text())
    global win
    win = window
    cursor.execute("SELECT (idx) FROM member WHERE title = %s", (roomtitle, ))
    global roomnum
    roomnum = int(cursor.fetchall[0][0])