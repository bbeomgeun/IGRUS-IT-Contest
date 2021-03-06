from PyQt5 import QtCore, QtGui, QtWidgets
from frameClick import framebutton

class roomButtons():
        def __init__(self, window):
            self.roombtn_2 = QtWidgets.QStackedWidget(window.main)
            self.roombtn_2.setStyleSheet("background-color: rgb(231, 230, 230);")
            self.roombtn_2.setObjectName("roombtn_2")
            self.page_3 = QtWidgets.QWidget()
            self.page_3.setObjectName("page_3")
            self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.page_3)
            self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_10.setSpacing(0)
            self.horizontalLayout_10.setObjectName("horizontalLayout_10")
            self.room_2 = framebutton(self.page_3)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.room_2.sizePolicy().hasHeightForWidth())
            self.room_2.setSizePolicy(sizePolicy)
            self.room_2.setMinimumSize(QtCore.QSize(0, 150))
            self.room_2.setStyleSheet("background-color: rgb(189, 215, 238);\n"
    "border-radius:30px;")
            self.room_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.room_2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.room_2.setObjectName("room_2")
            self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.room_2)
            self.horizontalLayout_17.setObjectName("horizontalLayout_17")
            self.roomImg_3 = QtWidgets.QLabel(self.room_2)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.roomImg_3.sizePolicy().hasHeightForWidth())
            self.roomImg_3.setSizePolicy(sizePolicy)
            self.roomImg_3.setMinimumSize(QtCore.QSize(110, 110))
            self.roomImg_3.setMaximumSize(QtCore.QSize(110, 110))
            self.roomImg_3.setAlignment(QtCore.Qt.AlignCenter)
            self.roomImg_3.setObjectName("roomImg_3")
            self.horizontalLayout_17.addWidget(self.roomImg_3)
            self.roomText_3 = QtWidgets.QFrame(self.room_2)
            self.roomText_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.roomText_3.setFrameShadow(QtWidgets.QFrame.Raised)
            self.roomText_3.setObjectName("roomText_3")
            self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.roomText_3)
            self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_7.setObjectName("verticalLayout_7")
            self.roomTitle_3 = QtWidgets.QLabel(self.roomText_3)
            font = QtGui.QFont()
            font.setFamily("나눔고딕")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.roomTitle_3.setFont(font)
            self.roomTitle_3.setAlignment(QtCore.Qt.AlignCenter)
            self.roomTitle_3.setObjectName("roomTitle_3")
            self.verticalLayout_7.addWidget(self.roomTitle_3)
            self.nameNnum_3 = QtWidgets.QFrame(self.roomText_3)
            self.nameNnum_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.nameNnum_3.setFrameShadow(QtWidgets.QFrame.Raised)
            self.nameNnum_3.setObjectName("nameNnum_3")
            self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.nameNnum_3)
            self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_11.setObjectName("horizontalLayout_11")
            self.num_3 = QtWidgets.QLabel(self.nameNnum_3)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.num_3.sizePolicy().hasHeightForWidth())
            self.num_3.setSizePolicy(sizePolicy)
            self.num_3.setMinimumSize(QtCore.QSize(200, 0))
            font = QtGui.QFont()
            font.setFamily("나눔고딕")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.num_3.setFont(font)
            self.num_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            self.num_3.setObjectName("num_3")
            self.horizontalLayout_11.addWidget(self.num_3)
            self.hostname_3 = QtWidgets.QLabel(self.nameNnum_3)
            font = QtGui.QFont()
            font.setFamily("나눔고딕")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.hostname_3.setFont(font)
            self.hostname_3.setAlignment(QtCore.Qt.AlignCenter)
            self.hostname_3.setObjectName("hostname_3")
            self.horizontalLayout_11.addWidget(self.hostname_3)
            self.verticalLayout_7.addWidget(self.nameNnum_3)
            self.horizontalLayout_17.addWidget(self.roomText_3)
            self.horizontalLayout_10.addWidget(self.room_2)
            self.roombtn_2.addWidget(self.page_3)
            self.page_4 = QtWidgets.QWidget()
            self.page_4.setObjectName("page_4")
            self.roombtn_2.addWidget(self.page_4)
            self.window = window
            self.roombtn_2.setCurrentIndex(1)


        def addWid(self, x, y):
            self.window.roomList.addWidget(self.roombtn_2, x, y, 1, 1)

        def showWid(self, title, hostname, num):
            self.roomTitle_3.setText(title)
            self.num_3.setText(hostname)
            self.hostname_3.setText(str(num) + "/5")
            self.roombtn_2.setCurrentIndex(0)
        
        def hideWid(self):
            self.roombtn_2.setCurrentIndex(1)

