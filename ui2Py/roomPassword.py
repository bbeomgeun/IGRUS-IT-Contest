from PyQt5 import QtCore, QtGui, QtWidgets
from source import windowButton
from movableWidget import movableWidget
from lineEditClick import lineEditbutton

class Ui_roomPassword(object):
    def setupUi(self, roomPassword):
        roomPassword.setObjectName("roomPassword")
        roomPassword.resize(350, 140)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(roomPassword.sizePolicy().hasHeightForWidth())
        roomPassword.setSizePolicy(sizePolicy)
        roomPassword.setMinimumSize(QtCore.QSize(350, 140))
        roomPassword.setMaximumSize(QtCore.QSize(350, 140))
        roomPassword.setStyleSheet("background-color: rgb(231, 230, 230);")
        roomPassword.setFrameShape(QtWidgets.QFrame.StyledPanel)
        roomPassword.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(roomPassword)
        self.verticalLayout.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.passwordbar = movableWidget(roomPassword)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordbar.sizePolicy().hasHeightForWidth())
        self.passwordbar.setSizePolicy(sizePolicy)
        self.passwordbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.passwordbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.passwordbar.setObjectName("passwordbar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.passwordbar)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.passwordTitle = QtWidgets.QLabel(self.passwordbar)
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
        self.horizontalLayout.addWidget(self.passwordTitle)
        self.passwordClose = QtWidgets.QPushButton(self.passwordbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordClose.sizePolicy().hasHeightForWidth())
        self.passwordClose.setSizePolicy(sizePolicy)
        self.passwordClose.setMinimumSize(QtCore.QSize(30, 30))
        self.passwordClose.setMaximumSize(QtCore.QSize(30, 30))
        self.passwordClose.setStyleSheet("QPushButton{\n"
"border-image: url(:/windowButton/closeDefault.PNG);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/windowButton/closeHover.png);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/windowButton/closePressed.png);\n"
"}\n"
"")
        self.passwordClose.setText("")
        self.passwordClose.setObjectName("passwordClose")
        self.horizontalLayout.addWidget(self.passwordClose)
        self.verticalLayout.addWidget(self.passwordbar)
        self.passwordFrame = QtWidgets.QFrame(roomPassword)
        self.passwordFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.passwordFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.passwordFrame.setObjectName("passwordFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.passwordFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.password = lineEditbutton(self.passwordFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setMinimumSize(QtCore.QSize(300, 60))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.password.setFont(font)
        self.password.setStyleSheet("border-radius: 25px;\n"
"color: rgb(175, 171, 171);\n"
"background-color: rgb(255, 255, 255);")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.horizontalLayout_2.addWidget(self.password)
        self.verticalLayout.addWidget(self.passwordFrame)

        self.retranslateUi(roomPassword)
        QtCore.QMetaObject.connectSlotsByName(roomPassword)

    def retranslateUi(self, roomPassword):
        _translate = QtCore.QCoreApplication.translate
        roomPassword.setWindowTitle(_translate("roomPassword", "Frame"))
        self.passwordTitle.setToolTip(_translate("roomPassword", "<html><head/><body><p><br/></p></body></html>"))
        self.passwordTitle.setText(_translate("roomPassword", "roomTitle"))
        self.password.setText(_translate("roomPassword", "암호를 입력해주세요"))

