from PyQt5 import QtCore, QtGui, QtWidgets

class myChat():
    def __init__(self, window):
        self.chatBox = QtWidgets.QFrame(window.chatContents)
        self.chatBox.setGeometry(QtCore.QRect(40, 30, 493, 65))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatBox.sizePolicy().hasHeightForWidth())
        self.chatBox.setSizePolicy(sizePolicy)
        self.chatBox.setMinimumSize(QtCore.QSize(0, 0))
        self.chatBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.chatBox.setObjectName("chatBox")
        self._2 = QtWidgets.QHBoxLayout(self.chatBox)
        self._2.setContentsMargins(0, 0, 0, 0)
        self._2.setSpacing(10)
        self._2.setObjectName("_2")
        spacerItem = QtWidgets.QSpacerItem(50, 50, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self._2.addItem(spacerItem)
        self.chat = QtWidgets.QTextBrowser(self.chatBox)
        self.chat.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chat.sizePolicy().hasHeightForWidth())
        self.chat.setSizePolicy(sizePolicy)
        self.chat.setMinimumSize(QtCore.QSize(0, 0))
        self.chat.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.chat.setFont(font)
        self.chat.setStyleSheet("border: 2px solid rgb(255, 170, 0);\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.chat.setObjectName("chat")
        self._2.addWidget(self.chat)
        self.me = QtWidgets.QFrame(self.chatBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.me.sizePolicy().hasHeightForWidth())
        self.me.setSizePolicy(sizePolicy)
        self.me.setMinimumSize(QtCore.QSize(60, 0))
        self.me.setObjectName("me")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.me)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(1)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.myImg = QtWidgets.QLabel(self.me)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.myImg.sizePolicy().hasHeightForWidth())
        self.myImg.setSizePolicy(sizePolicy)
        self.myImg.setMinimumSize(QtCore.QSize(60, 60))
        self.myImg.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.myImg.setFont(font)
        self.myImg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.myImg.setStyleSheet("border-radius: 30px;\n"
"background-color: rgb(255, 170, 0);")
        self.myImg.setAlignment(QtCore.Qt.AlignCenter)
        self.myImg.setObjectName("myImg")
        self.verticalLayout_14.addWidget(self.myImg)
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem1)
        self._2.addWidget(self.me)
        _translate = QtCore.QCoreApplication.translate
        self.chat.setText(_translate("MainWindow", "user님이 입장하셨습니다."))
        self.myImg.setText(_translate("MainWindow", ""))
        self.window = window

    def addWid(self, data, num):
        self.window.gridLayout_3.removeItem(self.window.spacerItem26)
        self.window.gridLayout_3.addWidget(self.chatBox, num, 0, 1, 1)#첫번째 숫자가 순서
        self.window.gridLayout_3.addItem(self.window.spacerItem26, num+1, 0, 1, 1)
        self.chat.setText(data)