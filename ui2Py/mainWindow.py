from PyQt5 import QtCore, QtGui, QtWidgets
from source import roomAddButton, slideButton, windowButton, refreshButton
from movableWidget import movableWidget
from lineEditClick import lineEditbutton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1002, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(1000, 700))
        self.stackedWidget.setStyleSheet("background-color: rgb(231, 230, 230);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.first = QtWidgets.QWidget()
        self.first.setObjectName("first")
        self.gridLayout = QtWidgets.QGridLayout(self.first)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.button = QtWidgets.QFrame(self.first)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button.sizePolicy().hasHeightForWidth())
        self.button.setSizePolicy(sizePolicy)
        self.button.setMinimumSize(QtCore.QSize(600, 100))
        self.button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button.setObjectName("button")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.button)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.join = QtWidgets.QPushButton(self.button)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.join.sizePolicy().hasHeightForWidth())
        self.join.setSizePolicy(sizePolicy)
        self.join.setMinimumSize(QtCore.QSize(280, 60))
        self.join.setMaximumSize(QtCore.QSize(230, 60))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.join.setFont(font)
        self.join.setStyleSheet("QPushButton{\n"
"background-color: rgb(189, 215, 238);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 191, 211);\n"
"}")
        self.join.setObjectName("join")
        self.horizontalLayout.addWidget(self.join)
        self.signin = QtWidgets.QPushButton(self.button)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signin.sizePolicy().hasHeightForWidth())
        self.signin.setSizePolicy(sizePolicy)
        self.signin.setMinimumSize(QtCore.QSize(290, 60))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.signin.setFont(font)
        self.signin.setStyleSheet("QPushButton{\n"
"background-color: rgb(189, 215, 238);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 191, 211);\n"
"}")
        self.signin.setObjectName("signin")
        self.horizontalLayout.addWidget(self.signin)
        self.gridLayout.addWidget(self.button, 8, 2, 1, 1)
        self.profileFrame = QtWidgets.QFrame(self.first)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileFrame.sizePolicy().hasHeightForWidth())
        self.profileFrame.setSizePolicy(sizePolicy)
        self.profileFrame.setMinimumSize(QtCore.QSize(600, 200))
        self.profileFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profileFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profileFrame.setObjectName("profileFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.profileFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.firstProfile = QtWidgets.QLabel(self.profileFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstProfile.sizePolicy().hasHeightForWidth())
        self.firstProfile.setSizePolicy(sizePolicy)
        self.firstProfile.setMinimumSize(QtCore.QSize(210, 210))
        self.firstProfile.setMaximumSize(QtCore.QSize(200, 200))
        self.firstProfile.setStyleSheet("border-radius: 100px;\n"
"background-color: rgb(242, 242, 242);\n"
"")
        self.firstProfile.setText("")
        self.firstProfile.setObjectName("firstProfile")
        self.horizontalLayout_2.addWidget(self.firstProfile)
        self.gridLayout.addWidget(self.profileFrame, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.input = QtWidgets.QFrame(self.first)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy)
        self.input.setMinimumSize(QtCore.QSize(600, 200))
        self.input.setMaximumSize(QtCore.QSize(600, 200))
        self.input.setStyleSheet("background-color: rgb(189, 215, 238);\n"
"border-radius:30px;")
        self.input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input.setObjectName("input")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.input)
        self.gridLayout_2.setContentsMargins(11, 15, 15, 15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.id = QtWidgets.QLabel(self.input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.id.sizePolicy().hasHeightForWidth())
        self.id.setSizePolicy(sizePolicy)
        self.id.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.id.setFont(font)
        self.id.setStyleSheet("background-color: rgb(189, 215, 238);")
        self.id.setAlignment(QtCore.Qt.AlignCenter)
        self.id.setObjectName("id")
        self.gridLayout_2.addWidget(self.id, 2, 1, 1, 1)
        self.inputpw = QtWidgets.QLineEdit(self.input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputpw.sizePolicy().hasHeightForWidth())
        self.inputpw.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.inputpw.setFont(font)
        self.inputpw.setMinimumSize(QtCore.QSize(50, 35))
        self.inputpw.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.inputpw.setText("")
        self.inputpw.setObjectName("inputpw")
        self.gridLayout_2.addWidget(self.inputpw, 4, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 3, 2, 1, 1)
        self.pw = QtWidgets.QLabel(self.input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pw.sizePolicy().hasHeightForWidth())
        self.pw.setSizePolicy(sizePolicy)
        self.pw.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pw.setFont(font)
        self.pw.setStyleSheet("background-color: rgb(189, 215, 238);\n"
"border-radius: 10px;")
        self.pw.setAlignment(QtCore.Qt.AlignCenter)
        self.pw.setObjectName("pw")
        self.gridLayout_2.addWidget(self.pw, 4, 1, 1, 1)
        self.inputid = QtWidgets.QLineEdit(self.input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputid.sizePolicy().hasHeightForWidth())
        self.inputid.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.inputid.setFont(font)
        self.inputid.setMinimumSize(QtCore.QSize(450, 35))
        self.inputid.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.inputid.setText("")
        self.inputid.setObjectName("inputid")
        self.gridLayout_2.addWidget(self.inputid, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.input, 3, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 4, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(10, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 9, 2, 1, 1)
        self.firstbar = movableWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstbar.sizePolicy().hasHeightForWidth())
        self.firstbar.setSizePolicy(sizePolicy)
        self.firstbar.setMinimumSize(QtCore.QSize(0, 50))
        self.firstbar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.firstbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.firstbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.firstbar.setObjectName("firstbar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.firstbar)
        self.horizontalLayout_3.setContentsMargins(-1, 13, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.firstMinimize = QtWidgets.QPushButton(self.firstbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstMinimize.sizePolicy().hasHeightForWidth())
        self.firstMinimize.setSizePolicy(sizePolicy)
        self.firstMinimize.setMinimumSize(QtCore.QSize(30, 30))
        self.firstMinimize.setMaximumSize(QtCore.QSize(30, 30))
        self.firstMinimize.setStyleSheet("QPushButton{\n"
"border-image: url(:/windowButton/minimizeDefault.PNG);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/windowButton/minimizeHover.png);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/windowButton/minimizePressed.png);\n"
"}\n"
"")
        self.firstMinimize.setText("")
        self.firstMinimize.setObjectName("firstMinimize")
        self.horizontalLayout_3.addWidget(self.firstMinimize)
        self.firstMaximize = QtWidgets.QPushButton(self.firstbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstMaximize.sizePolicy().hasHeightForWidth())
        self.firstMaximize.setSizePolicy(sizePolicy)
        self.firstMaximize.setMinimumSize(QtCore.QSize(30, 30))
        self.firstMaximize.setMaximumSize(QtCore.QSize(30, 30))
        self.firstMaximize.setStyleSheet("QPushButton{\n"
"border-image: url(:/windowButton/maximizeDefault.PNG);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/windowButton/maximizeHover.png);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/windowButton/maximizePressed.png);\n"
"}\n"
"")
        self.firstMaximize.setText("")
        self.firstMaximize.setObjectName("firstMaximize")
        self.horizontalLayout_3.addWidget(self.firstMaximize)
        self.firstClose = QtWidgets.QPushButton(self.firstbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstClose.sizePolicy().hasHeightForWidth())
        self.firstClose.setSizePolicy(sizePolicy)
        self.firstClose.setMinimumSize(QtCore.QSize(30, 30))
        self.firstClose.setMaximumSize(QtCore.QSize(30, 30))
        self.firstClose.setStyleSheet("QPushButton{\n"
"border-image: url(:/windowButton/closeDefault.PNG);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/windowButton/closeHover.png);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/windowButton/closePressed.png);\n"
"}\n"
"")
        self.firstClose.setText("")
        self.firstClose.setObjectName("firstClose")
        self.horizontalLayout_3.addWidget(self.firstClose)
        self.gridLayout.addWidget(self.firstbar, 0, 0, 1, 4)
        self.stackedWidget.addWidget(self.first)
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainbar = movableWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainbar.sizePolicy().hasHeightForWidth())
        self.mainbar.setSizePolicy(sizePolicy)
        self.mainbar.setMinimumSize(QtCore.QSize(0, 65))
        self.mainbar.setMaximumSize(QtCore.QSize(16777215, 60))
        self.mainbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainbar.setObjectName("mainbar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.mainbar)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mainProfile = QtWidgets.QLabel(self.mainbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainProfile.sizePolicy().hasHeightForWidth())
        self.mainProfile.setSizePolicy(sizePolicy)
        self.mainProfile.setMinimumSize(QtCore.QSize(60, 60))
        self.mainProfile.setMaximumSize(QtCore.QSize(60, 60))
        self.mainProfile.setStyleSheet("border-radius: 30px;\n"
"background-color: rgb(242, 242, 242);\n"
"")
        self.mainProfile.setText("")
        self.mainProfile.setObjectName("mainProfile")
        self.horizontalLayout_4.addWidget(self.mainProfile)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.mainUserInfo = QtWidgets.QPushButton(self.mainbar)
        self.mainUserInfo.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.mainUserInfo.setFont(font)
        self.mainUserInfo.setStyleSheet("QPushButton{\n"
"border: 0px;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"border: 0px;\n"
"color: rgb(157, 157, 157);\n"
"}\n"
"QPushButton:pressed{\n"
"color: rgb(168, 191, 211);\n"
"}")
        self.mainUserInfo.setObjectName("mainUserInfo")
        self.horizontalLayout_4.addWidget(self.mainUserInfo)
        spacerItem8 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.mainMinimize = QtWidgets.QPushButton(self.mainbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainMinimize.sizePolicy().hasHeightForWidth())
        self.mainMinimize.setSizePolicy(sizePolicy)
        self.mainMinimize.setMinimumSize(QtCore.QSize(30, 30))
        self.mainMinimize.setMaximumSize(QtCore.QSize(30, 30))
        self.mainMinimize.setStyleSheet("QPushButton{\n"
"border-image: url(:/windowButton/minimizeDefault.PNG);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/windowButton/minimizeHover.png);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/windowButton/minimizePressed.png);\n"
"}\n"
"")
        self.mainMinimize.setText("")
        self.mainMinimize.setObjectName("mainMinimize")
        self.horizontalLayout_4.addWidget(self.mainMinimize)
        self.mainMaximize = QtWidgets.QPushButton(self.mainbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainMaximize.sizePolicy().hasHeightForWidth())
        self.mainMaximize.setSizePolicy(sizePolicy)
        self.mainMaximize.setMinimumSize(QtCore.QSize(30, 30))
        self.mainMaximize.setMaximumSize(QtCore.QSize(30, 30))
        self.mainMaximize.setStyleSheet("QPushButton{\n"
"border-image: url(:/windowButton/maximizeDefault.PNG);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/windowButton/maximizeHover.png);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/windowButton/maximizePressed.png);\n"
"}\n"
"")
        self.mainMaximize.setText("")
        self.mainMaximize.setObjectName("mainMaximize")
        self.horizontalLayout_4.addWidget(self.mainMaximize)
        self.mainClose = QtWidgets.QPushButton(self.mainbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainClose.sizePolicy().hasHeightForWidth())
        self.mainClose.setSizePolicy(sizePolicy)
        self.mainClose.setMinimumSize(QtCore.QSize(30, 30))
        self.mainClose.setMaximumSize(QtCore.QSize(30, 30))
        self.mainClose.setStyleSheet("QPushButton{\n"
"border-image: url(:/windowButton/closeDefault.PNG);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/windowButton/closeHover.png);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/windowButton/closePressed.png);\n"
"}\n"
"")
        self.mainClose.setText("")
        self.mainClose.setObjectName("mainClose")
        self.horizontalLayout_4.addWidget(self.mainClose)
        self.verticalLayout_2.addWidget(self.mainbar)
        self.searchRoomFrame = QtWidgets.QHBoxLayout()
        self.searchRoomFrame.setObjectName("searchRoomFrame")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.searchRoomFrame.addItem(spacerItem9)
        self.searchRoom = lineEditbutton(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchRoom.sizePolicy().hasHeightForWidth())
        self.searchRoom.setSizePolicy(sizePolicy)
        self.searchRoom.setMinimumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.searchRoom.setFont(font)
        self.searchRoom.setStyleSheet("border-radius: 25px;\n"
"color: rgb(175, 171, 171);\n"
"background-color: rgb(255, 255, 255);")
        self.searchRoom.setAlignment(QtCore.Qt.AlignCenter)
        self.searchRoom.setObjectName("searchRoom")
        self.searchRoomFrame.addWidget(self.searchRoom)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.searchRoomFrame.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.searchRoomFrame)
        self.addRoomFrame = QtWidgets.QFrame(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addRoomFrame.sizePolicy().hasHeightForWidth())
        self.addRoomFrame.setSizePolicy(sizePolicy)
        self.addRoomFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.addRoomFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.addRoomFrame.setObjectName("addRoomFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.addRoomFrame)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.refreshButton = QtWidgets.QPushButton(self.addRoomFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshButton.sizePolicy().hasHeightForWidth())
        self.refreshButton.setSizePolicy(sizePolicy)
        self.refreshButton.setMinimumSize(QtCore.QSize(50, 50))
        self.refreshButton.setStyleSheet("QPushButton{\n"
"border-image: url(:/refreshButton/refreashDefault.png);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/refreshButton/refreashhover.png);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/refreshButton/refreashPressed.png);\n"
"}")
        self.refreshButton.setText("")
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout_6.addWidget(self.refreshButton)
        self.addRoom = QtWidgets.QPushButton(self.addRoomFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addRoom.sizePolicy().hasHeightForWidth())
        self.addRoom.setSizePolicy(sizePolicy)
        self.addRoom.setMinimumSize(QtCore.QSize(50, 50))
        self.addRoom.setStyleSheet("QPushButton{\n"
"border-image: url(:/addButton/roomAddDefault.PNG);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/addButton/roomAddHover.PNG);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/addButton/roomAddPressed.png);\n"
"}")
        self.addRoom.setText("")
        self.addRoom.setObjectName("addRoom")
        self.horizontalLayout_6.addWidget(self.addRoom)
        spacerItem12 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.verticalLayout_2.addWidget(self.addRoomFrame)
        self.roomList = QtWidgets.QGridLayout()
        self.roomList.setContentsMargins(10, 0, 10, 0)
        self.roomList.setSpacing(10)
        self.roomList.setObjectName("roomList")
        self.left = QtWidgets.QFrame(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left.sizePolicy().hasHeightForWidth())
        self.left.setSizePolicy(sizePolicy)
        self.left.setMaximumSize(QtCore.QSize(40, 16777215))
        self.left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left.setObjectName("left")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem13 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem13)
        self.goLeft = QtWidgets.QPushButton(self.left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goLeft.sizePolicy().hasHeightForWidth())
        self.goLeft.setSizePolicy(sizePolicy)
        self.goLeft.setMinimumSize(QtCore.QSize(20, 105))
        self.goLeft.setMaximumSize(QtCore.QSize(20, 16777215))
        self.goLeft.setSizeIncrement(QtCore.QSize(0, 0))
        self.goLeft.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.goLeft.setAutoFillBackground(False)
        self.goLeft.setStyleSheet("QPushButton{\n"
"    border-image: url(:/slideButton/leftSlideDefault.PNG);\n"
"}\n"
"QPushButton:hover{\n"
"    border-image: url(:/slideButton/leftSlideHover.PNG);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/slideButton/leftSlidePressed.png);\n"
"}")
        self.goLeft.setText("")
        self.goLeft.setIconSize(QtCore.QSize(20, 20))
        self.goLeft.setObjectName("goLeft")
        self.verticalLayout_3.addWidget(self.goLeft)
        spacerItem14 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem14)
        self.roomList.addWidget(self.left, 2, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.roomList.addItem(spacerItem15, 3, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.roomList.addItem(spacerItem16, 1, 4, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.roomList.addItem(spacerItem17, 5, 3, 1, 1)
        self.right = QtWidgets.QFrame(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right.sizePolicy().hasHeightForWidth())
        self.right.setSizePolicy(sizePolicy)
        self.right.setMaximumSize(QtCore.QSize(40, 16777215))
        self.right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right.setObjectName("right")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.right)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem18 = QtWidgets.QSpacerItem(0, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem18)
        self.goRight = QtWidgets.QPushButton(self.right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goRight.sizePolicy().hasHeightForWidth())
        self.goRight.setSizePolicy(sizePolicy)
        self.goRight.setMinimumSize(QtCore.QSize(20, 105))
        self.goRight.setMaximumSize(QtCore.QSize(20, 16777215))
        self.goRight.setStyleSheet("QPushButton{\n"
"border-image: url(:/slideButton/rightSlideDefault.PNG);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/slideButton/rightSlideHover.PNG);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/slideButton/rightSlidePressed.png);\n"
"}")
        self.goRight.setText("")
        self.goRight.setObjectName("goRight")
        self.verticalLayout_4.addWidget(self.goRight)
        spacerItem19 = QtWidgets.QSpacerItem(0, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem19)
        self.roomList.addWidget(self.right, 2, 4, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.roomList.addItem(spacerItem20, 4, 3, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.roomList.addItem(spacerItem21, 4, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.roomList)
        self.stackedWidget.addWidget(self.main)
        self.chat = QtWidgets.QWidget()
        self.chat.setObjectName("chat")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.chat)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.chatbar = movableWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatbar.sizePolicy().hasHeightForWidth())
        self.chatbar.setSizePolicy(sizePolicy)
        self.chatbar.setMinimumSize(QtCore.QSize(0, 65))
        self.chatbar.setMaximumSize(QtCore.QSize(16777215, 60))
        self.chatbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chatbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chatbar.setObjectName("chatbar")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.chatbar)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.chatProfile = QtWidgets.QLabel(self.chatbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatProfile.sizePolicy().hasHeightForWidth())
        self.chatProfile.setSizePolicy(sizePolicy)
        self.chatProfile.setMinimumSize(QtCore.QSize(60, 60))
        self.chatProfile.setMaximumSize(QtCore.QSize(60, 60))
        self.chatProfile.setStyleSheet("border-radius: 30px;\n"
"background-color: rgb(242, 242, 242);\n"
"")
        self.chatProfile.setText("")
        self.chatProfile.setObjectName("chatProfile")
        self.horizontalLayout_5.addWidget(self.chatProfile)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem22)
        self.chatUserInfo = QtWidgets.QPushButton(self.chatbar)
        self.chatUserInfo.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.chatUserInfo.setFont(font)
        self.chatUserInfo.setStyleSheet("QPushButton{\n"
"border: 0px;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"border: 0px;\n"
"color: rgb(157, 157, 157);\n"
"}\n"
"QPushButton:pressed{\n"
"color: rgb(168, 191, 211);\n"
"}")
        self.chatUserInfo.setObjectName("chatUserInfo")
        self.horizontalLayout_5.addWidget(self.chatUserInfo)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem23)
        self.chatRoomTitle = QtWidgets.QPushButton(self.chatbar)
        self.chatRoomTitle.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.chatRoomTitle.setFont(font)
        self.chatRoomTitle.setStyleSheet("QPushButton{\n"
"border: 0px;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"border: 0px;\n"
"color: rgb(157, 157, 157);\n"
"}\n"
"QPushButton:pressed{\n"
"color: rgb(168, 191, 211);\n"
"}")
        self.chatRoomTitle.setObjectName("chatRoomTitle")
        self.horizontalLayout_5.addWidget(self.chatRoomTitle)
        spacerItem24 = QtWidgets.QSpacerItem(250, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem24)
        self.chatMinimize = QtWidgets.QPushButton(self.chatbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatMinimize.sizePolicy().hasHeightForWidth())
        self.chatMinimize.setSizePolicy(sizePolicy)
        self.chatMinimize.setMinimumSize(QtCore.QSize(30, 30))
        self.chatMinimize.setMaximumSize(QtCore.QSize(30, 30))
        self.chatMinimize.setStyleSheet("QPushButton{\n"
"border-image: url(:/windowButton/minimizeDefault.PNG);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/windowButton/minimizeHover.png);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/windowButton/minimizePressed.png);\n"
"}")
        self.chatMinimize.setText("")
        self.chatMinimize.setObjectName("chatMinimize")
        self.horizontalLayout_5.addWidget(self.chatMinimize)
        self.chatMaximize = QtWidgets.QPushButton(self.chatbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatMaximize.sizePolicy().hasHeightForWidth())
        self.chatMaximize.setSizePolicy(sizePolicy)
        self.chatMaximize.setMinimumSize(QtCore.QSize(30, 30))
        self.chatMaximize.setMaximumSize(QtCore.QSize(30, 30))
        self.chatMaximize.setStyleSheet("QPushButton{\n"
"border-image: url(:/windowButton/maximizeDefault.PNG);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/windowButton/maximizeHover.png);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/windowButton/maximizePressed.png);\n"
"}\n"
"")
        self.chatMaximize.setText("")
        self.chatMaximize.setObjectName("chatMaximize")
        self.horizontalLayout_5.addWidget(self.chatMaximize)
        self.chatClose = QtWidgets.QPushButton(self.chatbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatClose.sizePolicy().hasHeightForWidth())
        self.chatClose.setSizePolicy(sizePolicy)
        self.chatClose.setMinimumSize(QtCore.QSize(30, 30))
        self.chatClose.setMaximumSize(QtCore.QSize(30, 30))
        self.chatClose.setStyleSheet("QPushButton{\n"
"border-image: url(:/windowButton/closeDefault.PNG);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/windowButton/closeHover.png);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/windowButton/closePressed.png);\n"
"}\n"
"")
        self.chatClose.setText("")
        self.chatClose.setObjectName("chatClose")
        self.horizontalLayout_5.addWidget(self.chatClose)
        self.verticalLayout_12.addWidget(self.chatbar)
        self.chatWindowFrame = QtWidgets.QFrame(self.chat)
        self.chatWindowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chatWindowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chatWindowFrame.setObjectName("chatWindowFrame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.chatWindowFrame)
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.chatPeople = QtWidgets.QFrame(self.chatWindowFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatPeople.sizePolicy().hasHeightForWidth())
        self.chatPeople.setSizePolicy(sizePolicy)
        self.chatPeople.setMinimumSize(QtCore.QSize(220, 590))
        self.chatPeople.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.chatPeople.setStyleSheet("background-color: rgb(118, 113, 113);\n"
"border-radius:25px;")
        self.chatPeople.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chatPeople.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chatPeople.setObjectName("chatPeople")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.chatPeople)
        self.verticalLayout_10.setContentsMargins(11, -1, 11, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.userInfo = QtWidgets.QFrame(self.chatPeople)
        self.userInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userInfo.setObjectName("userInfo")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.userInfo)
        self.horizontalLayout_14.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
#         self.chatImg = QtWidgets.QLabel(self.userInfo)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.chatImg.sizePolicy().hasHeightForWidth())
#         self.chatImg.setSizePolicy(sizePolicy)
#         self.chatImg.setMinimumSize(QtCore.QSize(60, 60))
#         self.chatImg.setMaximumSize(QtCore.QSize(60, 60))
#         self.chatImg.setStyleSheet("border-radius: 30px;\n"
# "background-color: rgb(255, 170, 0);")
#         self.chatImg.setObjectName("chatImg")
#         self.horizontalLayout_14.addWidget(self.chatImg)
        self.chatName = QtWidgets.QLabel(self.userInfo)
        self.chatName.setAlignment(QtCore.Qt.AlignCenter) 
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(60)
        self.chatName.setFont(font)
        self.chatName.setStyleSheet("color: rgb(255, 255, 255);")
        self.chatName.setObjectName("chatName")
        self.horizontalLayout_14.addWidget(self.chatName)
        self.verticalLayout_10.addWidget(self.userInfo)
        spacerItem25 = QtWidgets.QSpacerItem(20, 483, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem25)
        self.horizontalLayout_12.addWidget(self.chatPeople)
        self.chatWindow = QtWidgets.QFrame(self.chatWindowFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatWindow.sizePolicy().hasHeightForWidth())
        self.chatWindow.setSizePolicy(sizePolicy)
        self.chatWindow.setMinimumSize(QtCore.QSize(510, 590))
        self.chatWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.chatWindow.setStyleSheet("background-color: rgb(118, 113, 113);\n"
"border-radius:25px;")
        self.chatWindow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chatWindow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chatWindow.setObjectName("chatWindow")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.chatWindow)
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 11)
        self.verticalLayout_11.setSpacing(2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.menu = QtWidgets.QFrame(self.chatWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy)
        self.menu.setMinimumSize(QtCore.QSize(100, 70))
        self.menu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.menu.setSizeIncrement(QtCore.QSize(0, 0))
        self.menu.setStyleSheet("background-color: rgb(118, 113, 113);\n"
"border-radius:25px;")
        self.menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu.setObjectName("menu")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.menu)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(30)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.songInfo = QtWidgets.QLabel(self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songInfo.sizePolicy().hasHeightForWidth())
        self.songInfo.setSizePolicy(sizePolicy)
        self.songInfo.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.songInfo.setFont(font)
        self.songInfo.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(175, 171, 171);")
        self.songInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.songInfo.setObjectName("songInfo")
        self.horizontalLayout_15.addWidget(self.songInfo)
        self.exit = QtWidgets.QPushButton(self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy)
        self.exit.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setStyleSheet("QPushButton{\n"
"color:rgb(255, 255, 255);\n"
"background-color: rgb(175, 171, 171);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(157, 157, 157);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(231, 230, 230);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.exit.setObjectName("exit")
        self.horizontalLayout_15.addWidget(self.exit)
        self.verticalLayout_11.addWidget(self.menu)
        self.chatArea = QtWidgets.QScrollArea(self.chatWindow)
        self.chatArea.setWidgetResizable(True)
        self.chatArea.setObjectName("chatArea")
        self.chatArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.chatArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.chatContents = QtWidgets.QWidget()
        self.chatContents.setGeometry(QtCore.QRect(0, 0, 706, 480))
        self.chatContents.setObjectName("chatContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.chatContents)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 5)
        self.gridLayout_3.setSpacing(7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.spacerItem26 = QtWidgets.QSpacerItem(20, 9999999, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(self.spacerItem26, 2, 0, 1, 1)
        # self.gridLayout_3.removeItem(self.spacerItem26)
#         self.chatBox = QtWidgets.QFrame(self.chatContents)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.chatBox.sizePolicy().hasHeightForWidth())
#         self.chatBox.setSizePolicy(sizePolicy)
#         self.chatBox.setMinimumSize(QtCore.QSize(0, 65))
#         self.chatBox.setObjectName("chatBox")
#         self._2 = QtWidgets.QHBoxLayout(self.chatBox)
#         self._2.setContentsMargins(0, 0, 0, 0)
#         self._2.setSpacing(10)
#         self._2.setObjectName("_2")
#         self.chatUserBox = QtWidgets.QFrame(self.chatBox)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.chatUserBox.sizePolicy().hasHeightForWidth())
#         self.chatUserBox.setSizePolicy(sizePolicy)
#         self.chatUserBox.setMinimumSize(QtCore.QSize(60, 0))
#         self.chatUserBox.setObjectName("chatUserBox")
#         self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.chatUserBox)
#         self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_14.setSpacing(1)
#         self.verticalLayout_14.setObjectName("verticalLayout_14")
#         self.chatUserImg = QtWidgets.QLabel(self.chatUserBox)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.chatUserImg.sizePolicy().hasHeightForWidth())
#         self.chatUserImg.setSizePolicy(sizePolicy)
#         self.chatUserImg.setMinimumSize(QtCore.QSize(60, 60))
#         self.chatUserImg.setMaximumSize(QtCore.QSize(60, 60))
#         font = QtGui.QFont()
#         font.setStyleStrategy(QtGui.QFont.PreferDefault)
#         self.chatUserImg.setFont(font)
#         self.chatUserImg.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.chatUserImg.setStyleSheet("border-radius: 30px;\n"
# "background-color: rgb(255, 170, 0);")
#         self.chatUserImg.setAlignment(QtCore.Qt.AlignCenter)
#         self.chatUserImg.setObjectName("chatUserImg")
#         self.verticalLayout_14.addWidget(self.chatUserImg)
#         spacerItem27 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
#         self.verticalLayout_14.addItem(spacerItem27)
#         self._2.addWidget(self.chatUserBox)
#         self.chatting = QtWidgets.QLabel(self.chatBox)
#         self.chatting.setEnabled(True)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.chatting.sizePolicy().hasHeightForWidth())
#         self.chatting.setSizePolicy(sizePolicy)
#         self.chatting.setMinimumSize(QtCore.QSize(0, 60))
#         self.chatting.setMaximumSize(QtCore.QSize(16777215, 16777215))
#         font = QtGui.QFont()
#         font.setFamily("나눔고딕")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         font.setKerning(True)
#         font.setStyleStrategy(QtGui.QFont.PreferDefault)
#         self.chatting.setFont(font)
#         self.chatting.setStyleSheet("border: 2px solid rgb(255, 170, 0);\n"
# "border-radius: 10px;\n"
# "background-color: rgb(255, 255, 255);")
#         self.chatting.setObjectName("chatting")
#         self._2.addWidget(self.chatting)
#         spacerItem28 = QtWidgets.QSpacerItem(50, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self._2.addItem(spacerItem28)
#         self.gridLayout_3.addWidget(self.chatBox, 1, 0, 1, 1)
        self.chatArea.setWidget(self.chatContents)
        self.verticalLayout_11.addWidget(self.chatArea)
        self.chatInput = lineEditbutton(self.chatWindow)
        self.chatInput.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.chatInput.setFont(font)
        self.chatInput.setStyleSheet("background-color: rgb(175, 171, 171);\n"
"border-radius:15px;")
        self.chatInput.setText("")
        self.chatInput.setObjectName("chatInput")
        self.verticalLayout_11.addWidget(self.chatInput)
        self.horizontalLayout_12.addWidget(self.chatWindow)
        self.verticalLayout_12.addWidget(self.chatWindowFrame)
        self.stackedWidget.addWidget(self.chat)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.join.setText(_translate("MainWindow", "회원가입"))
        self.signin.setText(_translate("MainWindow", "로그인"))
        self.id.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.id.setText(_translate("MainWindow", "ID"))
        self.pw.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pw.setText(_translate("MainWindow", "PW"))
        self.mainUserInfo.setText(_translate("MainWindow", "User Info"))
        self.searchRoom.setText(_translate("MainWindow", "검색"))
        self.chatUserInfo.setText(_translate("MainWindow", "User Info"))
        self.chatRoomTitle.setText(_translate("MainWindow", "room Title"))
        # self.chatImg.setText(_translate("MainWindow", "img"))
        self.chatName.setText(_translate("(MainWindow", "도움말\n●search '검색어'●\n노래검색내용 5개를 \n보여줍니다.\
        \n●queue●\n현재 재생목록을 \n보여줍니다.\n●delete '숫자'●\n입력한 숫자번째에 있는 \n재생대기곡을 지웁니다.\n●repeat●\n현재곡을 한번 더 \n재생합니다.\
        \n●suffle●\n랜덤하게 재생합니다.\n●purge●\n재생목록을 \n초기화합니다.\n●volume '숫자'●\n숫자만큼의 소리로 \n조절합니다.\n●skip●\n현재곡을 건너뜁니다.\
        \n●pause●\n재생중인 곡을 \n일시정지합니다.)"))
        self.songInfo.setText(_translate("MainWindow", ""))
        self.exit.setText(_translate("MainWindow", "나가기"))
        # self.chatUserImg.setText(_translate("MainWindow", "img"))
        # self.chatting.setText(_translate("MainWindow", "user님이 입장하셨습니다."))

        
class sig(QtCore.QObject):
    userchatArrived = QtCore.pyqtSignal()
    mychatArrived = QtCore.pyqtSignal()
    makingRoom  = QtCore.pyqtSignal()
    
    def user(self):
        self.userchatArrived.emit()

    def my(self):
        self.mychatArrived.emit()

    def room(self):
        self.makingRoom.emit()
