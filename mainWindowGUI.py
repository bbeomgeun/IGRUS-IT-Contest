import mainWindow, roomButton
from youtubeStream import streamPlayer
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pymysql
import editUserInfoGUI, joinUserGUI, roomAddGUI, roomPasswordGUI, roomSettingGUI
import chatClient
from myChat import myChat
from userChat import userChat
import threading

class GUI():
    def __init__(self, ui):
        self.window = ui
        self.maxi = False
        self.stream = ''
        self.driver =''
        self.player = ''
        self.userChatList = []
        self.myChatList = []
        self.client = ''
        self.chatCount = 0
        self.sign = sign
        self.chatText = ''
        ###loginpage
        self.window.join.clicked.connect(lambda: joinUserGUI.show())
        self.window.signin.clicked.connect(self.login)
        ###chatpage
        self.window.chatUserInfo.clicked.connect(self.userinfoSetting)
        self.window.chatRoomTitle.clicked.connect(lambda: roomSettingGUI.show(self.window.chatRoomTitle.text()))
        self.window.chatInput.released.connect(self.check)
        #self.window.exit.clicked.connect(
        ###roompage
        self.window.searchRoom.clicked.connect(self.clickSearch)#searchbar is pressed by mouse
        self.window.searchRoom.released.connect(self.searchRoom)#press enter to search room
        #self.window.goRight.clicked.connect)#roomlist nextpage
        #self.window.goLeft.clicked.connect()#roomlist prevpage
        self.window.addRoom.clicked.connect(self.makeRoom)
        self.window.mainUserInfo.clicked.connect(lambda: editUserInfoGUI.show(self.window))
        self.window.refreshButton.clicked.connect(self.chatStart)
        ###titlebar button
        self.window.mainMinimize.clicked.connect(lambda: MainWindow.showMinimized())
        self.window.mainMaximize.clicked.connect(self.maxiCount)
        self.window.mainClose.clicked.connect(MainWindow.close)
        self.window.firstMinimize.clicked.connect(lambda: MainWindow.showMinimized())
        self.window.firstMaximize.clicked.connect(self.maxiCount)
        self.window.firstClose.clicked.connect(MainWindow.close)
        self.window.chatMinimize.clicked.connect(lambda: MainWindow.showMinimized())
        self.window.chatMaximize.clicked.connect(self.maxiCount)
        self.window.chatClose.clicked.connect(MainWindow.close)
        ##custom sig
        self.sign.mychatArrived.connect(self.writeMyChat)
        self.sign.userchatArrived.connect(self.writeUserChat)
        
    def check(self):
        self.client.checker = True

    def chatStart(self):
        self.window.stackedWidget.setCurrentIndex(2)
        self.client = chatClient.chat_Client(self.window, "범근", Gui, sign)
        self.client.start()

    def getText(self, text):
        self.chatText = text
        self.window.chatInput.clear()

    def writeUserChat(self):
        self.player.getCommend(self.chatText)
        self.userChatList.append(userChat(MainWindow, self.window))
        self.userChatList[self.chatCount].addWid(self.chatText, self.chatCount)
        self.chatCount += 1
        
    def writeMyChat(self):
        self.player.getCommend(self.chatText)##youtubeplayer get commend
        self.myChatList.append(myChat(MainWindow, self.window))
        self.myChatList[self.chatCount].addWid(self.chatText, self.chatCount)
        self.chatCount += 1

    def playerPrint(self, text):
        pass

    def userinfoSetting(self):
        roomSettingGUI.gui##set roomsetting
        roomSettingGUI.show(self.window)

    def updateMainWindow(self):

        con = pymysql.connect(
            user = 'IGRUS',
            password = 'igrus1234',
            host = '13.124.126.150',
            db = 'ICBM',
            charset= 'utf8'
        )

        ##set all db element

    def login(self):
        id = str(self.window.inputid.text())
        pw = str(self.window.inputpw.text())
        
        con = pymysql.connect(
            user = 'IGRUS',
            password = 'igrus1234',
            host = '13.124.126.150',
            db = 'ICBM',
            charset= 'utf8'
        )
        cursor = con.cursor()
        
        cursor.execute("SELECT * FROM member WHERE id = %s", (id, ))
        data = cursor.fetchall()
        if data == ():
            QtWidgets.QMessageBox.information(self.window.signin, "알림", "존재하지 않는 id 입니다")
            return 0
        if data[0][2] != pw:
            QtWidgets.QMessageBox.information(self.window.signin, "알림", "pw 오류")
            return 0
        self.window.stackedWidget.setCurrentIndex(1)
        self.player = streamPlayer(self.window)
        self.player.start()

    def maxiCount(self):
        if self.maxi == False:
            MainWindow.showMaximized()
            self.maxi = True
        elif self.maxi == True:
            MainWindow.showNormal()
            self.maxi = False

    def userinfo(self):
        pass
    def makeRoom(self):
        roomAddGUI.show()##open roomAdd

    def clickSearch(self):
        if (self.window.stackedWidget.currentIndex() != 1):
            pass
        elif (self.window.searchRoom.text() != "검색"):
            pass
        else:
            self.window.searchRoom.clear()

    def searchRoom(self):
        pass
        #get roominfo from db
        #infolist->각 요소별로 room객체에 뿌려줌
    

def make():
    while 1:
        if Gui.chatCount + 1 < len(Gui.myChatList):
            continue
        Gui.myChatList.append(myChat(MainWindow, ui))
        Gui.userChatList.append(userChat(MainWindow, ui))

if __name__=="__main__":
    sign = mainWindow.sig()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainWindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
    Gui = GUI(ui)##call mainwindow
    MainWindow.show()
    editUserInfoGUI.gui##set userinfoedit
    joinUserGUI.gui##set joinuser
    roomAddGUI.gui##set roomadd
    roomPasswordGUI.gui##set roompassword
    stream = streamPlayer(ui)##call player
    
    sys.exit(app.exec_())