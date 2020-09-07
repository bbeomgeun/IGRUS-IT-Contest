# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'roomAdd.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_roomAdd(object):
    def setupUi(self, roomAdd):
        roomAdd.setObjectName("roomAdd")
        roomAdd.resize(440, 470)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(roomAdd.sizePolicy().hasHeightForWidth())
        roomAdd.setSizePolicy(sizePolicy)
        roomAdd.setMinimumSize(QtCore.QSize(440, 470))
        roomAdd.setMaximumSize(QtCore.QSize(440, 470))
        roomAdd.setStyleSheet("background-color: rgb(231, 230, 230);")
        roomAdd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        roomAdd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(roomAdd)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.roomAddbar = QtWidgets.QFrame(roomAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roomAddbar.sizePolicy().hasHeightForWidth())
        self.roomAddbar.setSizePolicy(sizePolicy)
        self.roomAddbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.roomAddbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.roomAddbar.setObjectName("roomAddbar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.roomAddbar)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.roomAddTitle = QtWidgets.QLabel(self.roomAddbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roomAddTitle.sizePolicy().hasHeightForWidth())
        self.roomAddTitle.setSizePolicy(sizePolicy)
        self.roomAddTitle.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.roomAddTitle.setFont(font)
        self.roomAddTitle.setStyleSheet("")
        self.roomAddTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.roomAddTitle.setObjectName("roomAddTitle")
        self.horizontalLayout.addWidget(self.roomAddTitle)
        self.roomAddClose = QtWidgets.QPushButton(self.roomAddbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roomAddClose.sizePolicy().hasHeightForWidth())
        self.roomAddClose.setSizePolicy(sizePolicy)
        self.roomAddClose.setMinimumSize(QtCore.QSize(30, 30))
        self.roomAddClose.setMaximumSize(QtCore.QSize(30, 30))
        self.roomAddClose.setStyleSheet("QPushButton{\n"
"border-image: url(:/windowButton/closeDefault.PNG);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/windowButton/closeHover.png);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/windowButton/closePressed.png);\n"
"}\n"
"")
        self.roomAddClose.setText("")
        self.roomAddClose.setObjectName("roomAddClose")
        self.horizontalLayout.addWidget(self.roomAddClose)
        self.verticalLayout.addWidget(self.roomAddbar)
        self.nameFrame = QtWidgets.QFrame(roomAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameFrame.sizePolicy().hasHeightForWidth())
        self.nameFrame.setSizePolicy(sizePolicy)
        self.nameFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.nameFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.nameFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nameFrame.setObjectName("nameFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.nameFrame)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.roomnameTitle = QtWidgets.QLabel(self.nameFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roomnameTitle.sizePolicy().hasHeightForWidth())
        self.roomnameTitle.setSizePolicy(sizePolicy)
        self.roomnameTitle.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.roomnameTitle.setFont(font)
        self.roomnameTitle.setStyleSheet("")
        self.roomnameTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.roomnameTitle.setObjectName("roomnameTitle")
        self.horizontalLayout_3.addWidget(self.roomnameTitle)
        self.roomname = QtWidgets.QLineEdit(self.nameFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roomname.sizePolicy().hasHeightForWidth())
        self.roomname.setSizePolicy(sizePolicy)
        self.roomname.setMinimumSize(QtCore.QSize(300, 60))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.roomname.setFont(font)
        self.roomname.setStyleSheet("border-radius: 25px;\n"
"color: rgb(175, 171, 171);\n"
"background-color: rgb(255, 255, 255);")
        self.roomname.setText("")
        self.roomname.setAlignment(QtCore.Qt.AlignCenter)
        self.roomname.setObjectName("roomname")
        self.horizontalLayout_3.addWidget(self.roomname)
        self.verticalLayout.addWidget(self.nameFrame)
        self.profileTitle = QtWidgets.QLabel(roomAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileTitle.sizePolicy().hasHeightForWidth())
        self.profileTitle.setSizePolicy(sizePolicy)
        self.profileTitle.setMinimumSize(QtCore.QSize(100, 50))
        self.profileTitle.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.profileTitle.setFont(font)
        self.profileTitle.setStyleSheet("")
        self.profileTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.profileTitle.setObjectName("profileTitle")
        self.verticalLayout.addWidget(self.profileTitle)
        self.fileSelectFrame = QtWidgets.QFrame(roomAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileSelectFrame.sizePolicy().hasHeightForWidth())
        self.fileSelectFrame.setSizePolicy(sizePolicy)
        self.fileSelectFrame.setMinimumSize(QtCore.QSize(0, 60))
        self.fileSelectFrame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.fileSelectFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fileSelectFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fileSelectFrame.setObjectName("fileSelectFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.fileSelectFrame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_5.setSpacing(7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.findFile = QtWidgets.QPushButton(self.fileSelectFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.findFile.sizePolicy().hasHeightForWidth())
        self.findFile.setSizePolicy(sizePolicy)
        self.findFile.setMinimumSize(QtCore.QSize(130, 60))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(19)
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
        self.horizontalLayout_5.addWidget(self.findFile)
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
        self.horizontalLayout_5.addWidget(self.showDirection)
        self.verticalLayout.addWidget(self.fileSelectFrame)
        self.checkPasswordFrame = QtWidgets.QFrame(roomAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkPasswordFrame.sizePolicy().hasHeightForWidth())
        self.checkPasswordFrame.setSizePolicy(sizePolicy)
        self.checkPasswordFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.checkPasswordFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.checkPasswordFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.checkPasswordFrame.setObjectName("checkPasswordFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.checkPasswordFrame)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.passwordTitle = QtWidgets.QLabel(self.checkPasswordFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordTitle.sizePolicy().hasHeightForWidth())
        self.passwordTitle.setSizePolicy(sizePolicy)
        self.passwordTitle.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.passwordTitle.setFont(font)
        self.passwordTitle.setStyleSheet("")
        self.passwordTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordTitle.setObjectName("passwordTitle")
        self.horizontalLayout_2.addWidget(self.passwordTitle)
        self.checkPassword = QtWidgets.QPushButton(self.checkPasswordFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkPassword.sizePolicy().hasHeightForWidth())
        self.checkPassword.setSizePolicy(sizePolicy)
        self.checkPassword.setMinimumSize(QtCore.QSize(50, 50))
        self.checkPassword.setMaximumSize(QtCore.QSize(16777215, 50))
        self.checkPassword.setStyleSheet("QPushButton{\n"
"    border-image: url(:/unchecked/checkbox.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border-image: url(:/unchecked/checkboxHover.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-image: url(:/unchecked/checkboxPressed.png);\n"
"}")
        self.checkPassword.setText("")
        self.checkPassword.setObjectName("checkPassword")
        self.horizontalLayout_2.addWidget(self.checkPassword)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.checkPasswordFrame)
        self.passwordInputFrame = QtWidgets.QFrame(roomAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordInputFrame.sizePolicy().hasHeightForWidth())
        self.passwordInputFrame.setSizePolicy(sizePolicy)
        self.passwordInputFrame.setMinimumSize(QtCore.QSize(400, 75))
        self.passwordInputFrame.setMaximumSize(QtCore.QSize(400, 16777215))
        self.passwordInputFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.passwordInputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.passwordInputFrame.setObjectName("passwordInputFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.passwordInputFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.password = QtWidgets.QLineEdit(self.passwordInputFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setMinimumSize(QtCore.QSize(400, 60))
        self.password.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.password.setFont(font)
        self.password.setStyleSheet("border-radius: 25px;\n"
"color: rgb(175, 171, 171);\n"
"background-color: rgb(255, 255, 255);")
        self.password.setText("")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.horizontalLayout_4.addWidget(self.password)
        self.verticalLayout.addWidget(self.passwordInputFrame)
        self.roomAddButton = QtWidgets.QPushButton(roomAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roomAddButton.sizePolicy().hasHeightForWidth())
        self.roomAddButton.setSizePolicy(sizePolicy)
        self.roomAddButton.setMinimumSize(QtCore.QSize(0, 50))
        self.roomAddButton.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.roomAddButton.setFont(font)
        self.roomAddButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(189, 215, 238);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 191, 211);\n"
"}")
        self.roomAddButton.setObjectName("roomAddButton")
        self.verticalLayout.addWidget(self.roomAddButton)
        self.passwordInputFrame.raise_()
        self.roomAddbar.raise_()
        self.checkPasswordFrame.raise_()
        self.nameFrame.raise_()
        self.roomAddButton.raise_()
        self.profileTitle.raise_()
        self.fileSelectFrame.raise_()

        self.retranslateUi(roomAdd)
        QtCore.QMetaObject.connectSlotsByName(roomAdd)

    def retranslateUi(self, roomAdd):
        _translate = QtCore.QCoreApplication.translate
        roomAdd.setWindowTitle(_translate("roomAdd", "Frame"))
        self.roomAddTitle.setToolTip(_translate("roomAdd", "<html><head/><body><p><br/></p></body></html>"))
        self.roomAddTitle.setText(_translate("roomAdd", "방 만들기"))
        self.roomnameTitle.setToolTip(_translate("roomAdd", "<html><head/><body><p><br/></p></body></html>"))
        self.roomnameTitle.setText(_translate("roomAdd", "이름"))
        self.profileTitle.setToolTip(_translate("roomAdd", "<html><head/><body><p><br/></p></body></html>"))
        self.profileTitle.setText(_translate("roomAdd", "방 프로필 선택"))
        self.findFile.setText(_translate("roomAdd", "찾아보기"))
        self.passwordTitle.setToolTip(_translate("roomAdd", "<html><head/><body><p><br/></p></body></html>"))
        self.passwordTitle.setText(_translate("roomAdd", "비밀번호"))
        self.roomAddButton.setText(_translate("roomAdd", "확인"))
import checkbox_rc
import windowButton_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    roomAdd = QtWidgets.QFrame()
    ui = Ui_roomAdd()
    ui.setupUi(roomAdd)
    roomAdd.show()
    sys.exit(app.exec_())
