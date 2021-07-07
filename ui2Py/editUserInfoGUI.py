import editUserInfo
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pymysql


class GUI():
    def __init__(self, ui):
        self.window = ui
        self.needCheck = False
        self.idExist = False
        self.idcheckClicked = True
        self.id = ''
        # cursor.execute("SELECT * FROM member WHERE id = %s", (self.id, ))
        # self.pw = cursor.fetchall()[0][2]
        self.window.check.clicked.connect(self.idDuplicationCheck)
        self.window.editClose.clicked.connect(edit.close)
        self.window.findFile.clicked.connect(self.getFile)
        self.window.leave.clicked.connect(self.leave)
        self.window.editClose.clicked.connect(edit.close)
        self.window.confirm.clicked.connect(self.confirm)
        self.window.inputid.setText(self.id)
        self.window.checkMessage.setText("동일 ID")

    def confirm(self):
        # if idcheckClicked and :
        #     self.window.checkMessage.setText("아이디 중복체크를 해주세요.")

        if self.needCheck:
            data = cursor.fetchall()[0]
            self.msg = QtWidgets.QMessageBox()
            self.msg.setWindowTitle("need check")
            self.msg.setText("아이디 중복체크를 해주세요.")
            self.msg.exec_()
        else:
            self.registerId = self.window.inputid.text()
            self.registerPw = self.window.inputpw.text()
            self.sql = "INSERT INTO member(id, pw, image) VALUES(%s, %s, %s)"
            cursor.execute(self.sql, (self.registerId, self.registerPw, self.inputFilePath, ))
            con.commit()
            self.msg = QtWidgets.QMessageBox()
            self.msg.setWindowTitle("register OK")
            self.msg.setText("회원가입 완료")
            self.msg.exec_()
        
    def leave(self):
        reply = QtWidgets.QMessageBox.question(self.window.leave, "알림", "정말 탈퇴하시겠습니까???", \
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            edit.close()
            mainwin.stackedWidget.setCurrentIndex(0)
            ##delete userinfo
        else:
            return 0

    def getFile(self):
        self.filePath = QtWidgets.QFileDialog.getOpenFileName()
        self.inputFilePath = self.filePath[0]
        self.realName = self.filePath[0].split('/')
        self.window.showDirection.setText(self.realName[len(self.realName) - 1])

    def idDuplicationCheck(self): # 아이디 중복확인
        self.idcheckClicked = True
        registerId = self.window.inputid.text()
        self.idExist = False
        self.sql = "SELECT id FROM member"
        cursor.execute(self.sql)

        for row in cursor.fetchall():
            if (row[0] == registerId):
                self.idExist = True
                break

        if self.idExist and registerId != self.id:
            self.window.checkMessage.setText("이미 사용중인 아이디입니다.")
            self.window.checkMessage.setStyleSheet("border: 2px solid black;\n"
"font: 11pt '나눔고딕';\n"
"border-radius:20px;")
        elif self.idExist and registerId == self.id:
            self.idExist = False
            return 0
        else:
            self.window.checkMessage.setText("사용 가능한 아이디입니다.")
            self.window.checkMessage.setStyleSheet("border: 2px solid black;\n"
"font: 12pt '나눔고딕';\n"
"border-radius:20px;")
            self.idExist = False
            self.needCheck = True

        
if __name__ != "__main__":
    global mainwin
    con = pymysql.connect(
        user = 'IGRUS',
        password = 'igrus1234',
        host = '13.124.126.150',
        db = 'ICBM',
        charset= 'utf8'
    )
    cursor = con.cursor()
    ##connect db
    app = QtWidgets.QApplication(sys.argv)
    edit = QtWidgets.QFrame()
    ui = editUserInfo.Ui_edit()
    ui.setupUi(edit)
    edit.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
    gui = GUI(ui)


def show(mainWin):
    edit.show()
    global mainwin
    mainwin = mainWin
    