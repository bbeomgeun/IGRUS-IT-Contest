from PyQt5 import QtCore, QtGui, QtWidgets
from source import windowButton
import joinUser
import pymysql
import sys

class GUIClass():
    def __init__(self, ui):
        self.window = ui
        self.isChecked = False
        self.inputFilePath = ""

        self.window.check.clicked.connect(self.idDuplicationCheck)
        self.window.findFile.clicked.connect(self.getFile)
        self.window.confirm.clicked.connect(self.register)
        self.window.joinClose.clicked.connect(lambda: join.close())

    def idDuplicationCheck(self): # 아이디 중복확인
        self.registerId = self.window.inputid.text()
        self.idExist = False
        self.sql = "SELECT id FROM member"
        cursor.execute(self.sql)

        for row in cursor.fetchall():
            if (row[0] == self.registerId):
                self.idExist = True
                break
        
        if self.idExist:
            self.window.checkMessage.setText("이미 사용중인 아이디입니다.")
            self.window.checkMessage.setStyleSheet("border: 2px solid black;\n"
"font: 11pt '나눔고딕';\n"
"border-radius:20px;")
        else:
            self.window.checkMessage.setText("사용 가능한 아이디입니다.")
            self.window.checkMessage.setStyleSheet("border: 2px solid black;\n"
"font: 12pt '나눔고딕';\n"
"border-radius:20px;")
            self.isChecked = True

    def getFile(self):
        self.filePath = QtWidgets.QFileDialog.getOpenFileName()
        self.inputFilePath = self.filePath[0]
        self.realName = self.filePath[0].split('/')
        self.window.showDirection.setText(self.realName[len(self.realName) - 1])

    def register(self):
        if not self.isChecked:
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

if __name__ != "__main__":

    con = pymysql.connect(
        user = 'IGRUS',
        password = 'igrus1234',
        host = '13.124.126.150',
        db = 'ICBM',
        charset= 'utf8'
    )
    cursor = con.cursor()
    cursor.execute("SELECT * FROM member")
    print(cursor.fetchall())
    app = QtWidgets.QApplication(sys.argv)
    join = QtWidgets.QFrame()
    ui = joinUser.Ui_join()
    ui.setupUi(join)
    join.setWindowFlags(QtCore.Qt.CustomizeWindowHint)

    gui = GUIClass(ui)

    # sys.exit(app.exec_())

def show():
    join.show()
