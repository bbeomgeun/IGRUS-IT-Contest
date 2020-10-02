from PyQt5 import QtCore, QtGui, QtWidgets
from source import windowButton
from movableWidget import movableWidget

class Ui_join(object):
    def setupUi(self, join):
        join.setObjectName("join")
        join.resize(400, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(join.sizePolicy().hasHeightForWidth())
        join.setSizePolicy(sizePolicy)
        join.setMinimumSize(QtCore.QSize(400, 500))
        join.setMaximumSize(QtCore.QSize(400, 500))
        join.setStyleSheet("background-color: rgb(231, 230, 230);")
        join.setFrameShape(QtWidgets.QFrame.StyledPanel)
        join.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(join)
        self.verticalLayout.setContentsMargins(5, 0, 5, 11)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.joinbar = movableWidget(join)
        self.joinbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.joinbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.joinbar.setObjectName("joinbar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.joinbar)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.joinTitle = QtWidgets.QLabel(self.joinbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.joinTitle.sizePolicy().hasHeightForWidth())
        self.joinTitle.setSizePolicy(sizePolicy)
        self.joinTitle.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.joinTitle.setFont(font)
        self.joinTitle.setStyleSheet("")
        self.joinTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.joinTitle.setObjectName("joinTitle")
        self.horizontalLayout.addWidget(self.joinTitle)
        spacerItem1 = QtWidgets.QSpacerItem(70, 0, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.joinClose = QtWidgets.QPushButton(self.joinbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.joinClose.sizePolicy().hasHeightForWidth())
        self.joinClose.setSizePolicy(sizePolicy)
        self.joinClose.setMinimumSize(QtCore.QSize(30, 30))
        self.joinClose.setMaximumSize(QtCore.QSize(30, 30))
        self.joinClose.setStyleSheet("QPushButton{\n"
"border-image: url(:/windowButton/closeDefault.PNG);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/windowButton/closeHover.png);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/windowButton/closePressed.png);\n"
"}\n"
"")
        self.joinClose.setText("")
        self.joinClose.setObjectName("joinClose")
        self.horizontalLayout.addWidget(self.joinClose)
        self.verticalLayout.addWidget(self.joinbar)
        self.idFrame = QtWidgets.QFrame(join)
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
        self.idCheckFrame = QtWidgets.QFrame(join)
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
        self.checkMessage.setAlignment(QtCore.Qt.AlignCenter)
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
        self.pwFrame = QtWidgets.QFrame(join)
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
        self.inputpw.setMinimumSize(QtCore.QSize(239, 60))
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
        self.profileTitle = QtWidgets.QLabel(join)
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
        self.fileSelectFrame = QtWidgets.QFrame(join)
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
        self.confirm = QtWidgets.QPushButton(join)
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
        self.verticalLayout.addWidget(self.confirm)

        self.retranslateUi(join)
        QtCore.QMetaObject.connectSlotsByName(join)

    def retranslateUi(self, join):
        _translate = QtCore.QCoreApplication.translate
        join.setWindowTitle(_translate("join", "Frame"))
        self.joinTitle.setToolTip(_translate("join", "<html><head/><body><p><br/></p></body></html>"))
        self.joinTitle.setText(_translate("join", "회원가입"))
        self.id.setToolTip(_translate("join", "<html><head/><body><p><br/></p></body></html>"))
        self.id.setText(_translate("join", "ID"))
        self.check.setText(_translate("join", "중복확인"))
        self.checkMessage.setText(_translate("join", "ID체크가 필요합니다!"))
        self.pw.setToolTip(_translate("join", "<html><head/><body><p><br/></p></body></html>"))
        self.pw.setText(_translate("join", "PW"))
        self.profileTitle.setToolTip(_translate("join", "<html><head/><body><p><br/></p></body></html>"))
        self.profileTitle.setText(_translate("join", "프로필 선택"))
        self.findFile.setText(_translate("join", "찾아보기"))
        self.confirm.setText(_translate("join", "확인"))