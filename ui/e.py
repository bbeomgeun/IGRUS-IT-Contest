# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editUserInfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_edit(object):
    def setupUi(self, edit):
        edit.setObjectName("edit")
        edit.resize(400, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(edit.sizePolicy().hasHeightForWidth())
        edit.setSizePolicy(sizePolicy)
        edit.setMinimumSize(QtCore.QSize(400, 500))
        edit.setMaximumSize(QtCore.QSize(400, 500))
        edit.setStyleSheet("background-color: rgb(231, 230, 230);")
        edit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        edit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(edit)
        self.verticalLayout.setContentsMargins(5, 0, 5, 11)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.editbar = QtWidgets.QFrame(edit)
        self.editbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.editbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.editbar.setObjectName("editbar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.editbar)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.editTitle = QtWidgets.QLabel(self.editbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editTitle.sizePolicy().hasHeightForWidth())
        self.editTitle.setSizePolicy(sizePolicy)
        self.editTitle.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.editTitle.setFont(font)
        self.editTitle.setStyleSheet("")
        self.editTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.editTitle.setObjectName("editTitle")
        self.horizontalLayout.addWidget(self.editTitle)
        spacerItem1 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.editClose = QtWidgets.QPushButton(self.editbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editClose.sizePolicy().hasHeightForWidth())
        self.editClose.setSizePolicy(sizePolicy)
        self.editClose.setMinimumSize(QtCore.QSize(30, 30))
        self.editClose.setMaximumSize(QtCore.QSize(30, 30))
        self.editClose.setStyleSheet("QPushButton{\n"
"border-image: url(:/windowButton/closeDefault.PNG);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/windowButton/closeHover.png);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/windowButton/closePressed.png);\n"
"}\n"
"")
        self.editClose.setText("")
        self.editClose.setObjectName("editClose")
        self.horizontalLayout.addWidget(self.editClose)
        self.verticalLayout.addWidget(self.editbar)
        self.idFrame = QtWidgets.QFrame(edit)
        self.idFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.idFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.idFrame.setObjectName("idFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.idFrame)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.id = QtWidgets.QLabel(self.idFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.id.sizePolicy().hasHeightForWidth())
        self.id.setSizePolicy(sizePolicy)
        self.id.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.id.setFont(font)
        self.id.setStyleSheet("")
        self.id.setAlignment(QtCore.Qt.AlignCenter)
        self.id.setObjectName("id")
        self.horizontalLayout_2.addWidget(self.id)
        self.inputid = QtWidgets.QLineEdit(self.idFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputid.sizePolicy().hasHeightForWidth())
        self.inputid.setSizePolicy(sizePolicy)
        self.inputid.setMinimumSize(QtCore.QSize(239, 60))
        self.inputid.setMaximumSize(QtCore.QSize(239, 16777215))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(18)
        self.inputid.setFont(font)
        self.inputid.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.inputid.setText("")
        self.inputid.setObjectName("inputid")
        self.horizontalLayout_2.addWidget(self.inputid)
        self.verticalLayout.addWidget(self.idFrame)
        self.idCheckFrame = QtWidgets.QFrame(edit)
        self.idCheckFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.idCheckFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.idCheckFrame.setObjectName("idCheckFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.idCheckFrame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.check = QtWidgets.QPushButton(self.idCheckFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check.sizePolicy().hasHeightForWidth())
        self.check.setSizePolicy(sizePolicy)
        self.check.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.check.setFont(font)
        self.check.setStyleSheet("QPushButton{\n"
"background-color: rgb(189, 215, 238);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 191, 211);\n"
"}")
        self.check.setObjectName("check")
        self.horizontalLayout_5.addWidget(self.check)
        self.checkMessage = QtWidgets.QLabel(self.idCheckFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkMessage.sizePolicy().hasHeightForWidth())
        self.checkMessage.setSizePolicy(sizePolicy)
        self.checkMessage.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.checkMessage.setFont(font)
        self.checkMessage.setStyleSheet("border: 2px solid black;\n"
"border-radius:20px;")
        self.checkMessage.setObjectName("checkMessage")
        self.horizontalLayout_5.addWidget(self.checkMessage)
        self.verticalLayout.addWidget(self.idCheckFrame)
        self.pwFrame = QtWidgets.QFrame(edit)
        self.pwFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pwFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pwFrame.setObjectName("pwFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.pwFrame)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pw = QtWidgets.QLabel(self.pwFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pw.sizePolicy().hasHeightForWidth())
        self.pw.setSizePolicy(sizePolicy)
        self.pw.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pw.setFont(font)
        self.pw.setStyleSheet("")
        self.pw.setAlignment(QtCore.Qt.AlignCenter)
        self.pw.setObjectName("pw")
        self.horizontalLayout_3.addWidget(self.pw)
        self.inputpw = QtWidgets.QLineEdit(self.pwFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputpw.sizePolicy().hasHeightForWidth())
        self.inputpw.setSizePolicy(sizePolicy)
        self.inputpw.setMinimumSize(QtCore.QSize(180, 60))
        self.inputpw.setMaximumSize(QtCore.QSize(239, 16777215))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(18)
        self.inputpw.setFont(font)
        self.inputpw.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.inputpw.setText("")
        self.inputpw.setObjectName("inputpw")
        self.horizontalLayout_3.addWidget(self.inputpw)
        self.verticalLayout.addWidget(self.pwFrame)
        self.profileTitle = QtWidgets.QLabel(edit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileTitle.sizePolicy().hasHeightForWidth())
        self.profileTitle.setSizePolicy(sizePolicy)
        self.profileTitle.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.profileTitle.setFont(font)
        self.profileTitle.setStyleSheet("")
        self.profileTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.profileTitle.setObjectName("profileTitle")
        self.verticalLayout.addWidget(self.profileTitle)
        self.fileSelectFrame = QtWidgets.QFrame(edit)
        self.fileSelectFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fileSelectFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fileSelectFrame.setObjectName("fileSelectFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.fileSelectFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.findFile = QtWidgets.QPushButton(self.fileSelectFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.findFile.sizePolicy().hasHeightForWidth())
        self.findFile.setSizePolicy(sizePolicy)
        self.findFile.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.findFile.setFont(font)
        self.findFile.setStyleSheet("QPushButton{\n"
"background-color: rgb(189, 215, 238);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 191, 211);\n"
"}")
        self.findFile.setObjectName("findFile")
        self.horizontalLayout_4.addWidget(self.findFile)
        self.showDirection = QtWidgets.QLabel(self.fileSelectFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showDirection.sizePolicy().hasHeightForWidth())
        self.showDirection.setSizePolicy(sizePolicy)
        self.showDirection.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.showDirection.setFont(font)
        self.showDirection.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.showDirection.setText("")
        self.showDirection.setObjectName("showDirection")
        self.horizontalLayout_4.addWidget(self.showDirection)
        self.verticalLayout.addWidget(self.fileSelectFrame)
        self.buttonFrame = QtWidgets.QFrame(edit)
        self.buttonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonFrame.setObjectName("buttonFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.buttonFrame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.leave = QtWidgets.QPushButton(self.buttonFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leave.sizePolicy().hasHeightForWidth())
        self.leave.setSizePolicy(sizePolicy)
        self.leave.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.leave.setFont(font)
        self.leave.setStyleSheet("QPushButton{\n"
"background-color: rgb(189, 215, 238);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 191, 211);\n"
"}")
        self.leave.setObjectName("leave")
        self.horizontalLayout_6.addWidget(self.leave)
        self.confirm = QtWidgets.QPushButton(self.buttonFrame)
        self.confirm.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.confirm.setFont(font)
        self.confirm.setStyleSheet("QPushButton{\n"
"background-color: rgb(189, 215, 238);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 191, 211);\n"
"}")
        self.confirm.setObjectName("confirm")
        self.horizontalLayout_6.addWidget(self.confirm)
        self.verticalLayout.addWidget(self.buttonFrame)

        self.retranslateUi(edit)
        QtCore.QMetaObject.connectSlotsByName(edit)

    def retranslateUi(self, edit):
        _translate = QtCore.QCoreApplication.translate
        edit.setWindowTitle(_translate("edit", "Frame"))
        self.editTitle.setToolTip(_translate("edit", "<html><head/><body><p><br/></p></body></html>"))
        self.editTitle.setText(_translate("edit", "회원정보 수정"))
        self.id.setToolTip(_translate("edit", "<html><head/><body><p><br/></p></body></html>"))
        self.id.setText(_translate("edit", "ID"))
        self.check.setText(_translate("edit", "중복확인"))
        self.checkMessage.setText(_translate("edit", "ID체크가 필요합니다!"))
        self.pw.setToolTip(_translate("edit", "<html><head/><body><p><br/></p></body></html>"))
        self.pw.setText(_translate("edit", "PW"))
        self.profileTitle.setToolTip(_translate("edit", "<html><head/><body><p><br/></p></body></html>"))
        self.profileTitle.setText(_translate("edit", "프로필 선택"))
        self.findFile.setText(_translate("edit", "찾아보기"))
        self.leave.setText(_translate("edit", "탈퇴"))
        self.confirm.setText(_translate("edit", "확인"))
import roomAddButton_rc
import slideButton_rc
import windowButton_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    edit = QtWidgets.QFrame()
    ui = Ui_edit()
    ui.setupUi(edit)
    edit.show()
    sys.exit(app.exec_())
