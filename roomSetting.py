from PyQt5 import QtCore, QtGui, QtWidgets
from source import checkbox
from source import windowButton
from movableWidget import movableWidget

class Ui_roomSetting(object):
    def setupUi(self, roomSetting):
        roomSetting.setObjectName("roomSetting")
        roomSetting.resize(440, 470)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(roomSetting.sizePolicy().hasHeightForWidth())
        roomSetting.setSizePolicy(sizePolicy)
        roomSetting.setMinimumSize(QtCore.QSize(440, 470))
        roomSetting.setMaximumSize(QtCore.QSize(440, 470))
        roomSetting.setStyleSheet("background-color: rgb(231, 230, 230);")
        roomSetting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        roomSetting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(roomSetting)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.roomSettingbar = movableWidget(roomSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roomSettingbar.sizePolicy().hasHeightForWidth())
        self.roomSettingbar.setSizePolicy(sizePolicy)
        self.roomSettingbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.roomSettingbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.roomSettingbar.setObjectName("roomSettingbar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.roomSettingbar)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.roomSettingTitle = QtWidgets.QLabel(self.roomSettingbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roomSettingTitle.sizePolicy().hasHeightForWidth())
        self.roomSettingTitle.setSizePolicy(sizePolicy)
        self.roomSettingTitle.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.roomSettingTitle.setFont(font)
        self.roomSettingTitle.setStyleSheet("")
        self.roomSettingTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.roomSettingTitle.setObjectName("roomSettingTitle")
        self.horizontalLayout.addWidget(self.roomSettingTitle)
        self.roomSettingClose = QtWidgets.QPushButton(self.roomSettingbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roomSettingClose.sizePolicy().hasHeightForWidth())
        self.roomSettingClose.setSizePolicy(sizePolicy)
        self.roomSettingClose.setMinimumSize(QtCore.QSize(30, 30))
        self.roomSettingClose.setMaximumSize(QtCore.QSize(30, 30))
        self.roomSettingClose.setStyleSheet("QPushButton{\n"
"border-image: url(:/windowButton/closeDefault.PNG);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/windowButton/closeHover.png);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/windowButton/closePressed.png);\n"
"}\n"
"")
        self.roomSettingClose.setText("")
        self.roomSettingClose.setObjectName("roomSettingClose")
        self.horizontalLayout.addWidget(self.roomSettingClose)
        self.verticalLayout.addWidget(self.roomSettingbar)
        self.nameFrame = QtWidgets.QFrame(roomSetting)
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
        self.profileTitle = QtWidgets.QLabel(roomSetting)
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
        self.fileSelectFrame = QtWidgets.QFrame(roomSetting)
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
        self.checkPasswordFrame = QtWidgets.QFrame(roomSetting)
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
        self.passwordInputFrame = QtWidgets.QFrame(roomSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordInputFrame.sizePolicy().hasHeightForWidth())
        self.passwordInputFrame.setSizePolicy(sizePolicy)
        self.passwordInputFrame.setMinimumSize(QtCore.QSize(400, 0))
        self.passwordInputFrame.setMaximumSize(QtCore.QSize(400, 0))
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
        self.roomSettingButton = QtWidgets.QPushButton(roomSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roomSettingButton.sizePolicy().hasHeightForWidth())
        self.roomSettingButton.setSizePolicy(sizePolicy)
        self.roomSettingButton.setMinimumSize(QtCore.QSize(0, 50))
        self.roomSettingButton.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.roomSettingButton.setFont(font)
        self.roomSettingButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(189, 215, 238);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 191, 211);\n"
"}")
        self.roomSettingButton.setObjectName("roomSettingButton")
        self.verticalLayout.addWidget(self.roomSettingButton)
        self.passwordInputFrame.raise_()
        self.roomSettingbar.raise_()
        self.checkPasswordFrame.raise_()
        self.nameFrame.raise_()
        self.roomSettingButton.raise_()
        self.profileTitle.raise_()
        self.fileSelectFrame.raise_()

        self.retranslateUi(roomSetting)
        QtCore.QMetaObject.connectSlotsByName(roomSetting)

    def retranslateUi(self, roomSetting):
        _translate = QtCore.QCoreApplication.translate
        roomSetting.setWindowTitle(_translate("roomSetting", "Frame"))
        self.roomSettingTitle.setToolTip(_translate("roomSetting", "<html><head/><body><p><br/></p></body></html>"))
        self.roomSettingTitle.setText(_translate("roomSetting", "방 정보 수정"))
        self.roomnameTitle.setToolTip(_translate("roomSetting", "<html><head/><body><p><br/></p></body></html>"))
        self.roomnameTitle.setText(_translate("roomSetting", "이름"))
        self.profileTitle.setToolTip(_translate("roomSetting", "<html><head/><body><p><br/></p></body></html>"))
        self.profileTitle.setText(_translate("roomSetting", "방 프로필 선택"))
        self.findFile.setText(_translate("roomSetting", "찾아보기"))
        self.passwordTitle.setToolTip(_translate("roomSetting", "<html><head/><body><p><br/></p></body></html>"))
        self.passwordTitle.setText(_translate("roomSetting", "비밀번호"))
        self.roomSettingButton.setText(_translate("roomSetting", "확인"))

        