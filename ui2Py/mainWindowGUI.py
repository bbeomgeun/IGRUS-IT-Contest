import mainWindow, roomButton
from youtubeStream import streamPlayer
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pymysql
import editUserInfoGUI, joinUserGUI, roomAddGUI, roomPasswordGUI, roomSettingGUI
import chatClient
from roomButton import roomButtons
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
        self.ishost = False
        self.id = ''


        self.pageNum = 1   # 현재 페이지 지정
        self.startIndex = 0   # 각 페이지에서 데이터베이스 값의 시작 인덱스 지정
        self.data = []                                           # index[0][1]은 첫 번째 row의 첫번째 column 값을 의미 (column 중 id는 식별자이기 때문에 무시됨)
        self.maxPage = 1   # 데이터 개수에 따라 마지막 페이지 지정
        self.dataNumRest = 0   # 마지막 페이지에 존재하는 데이터의 개수


        ###loginpage
        self.window.join.clicked.connect(lambda: joinUserGUI.show())
        self.window.signin.clicked.connect(self.login)
        self.window.inputpw.setEchoMode(2)
        ###chatpage
        # self.window.chatUserInfo.clicked.connect(self.userinfo)
        self.window.chatRoomTitle.clicked.connect(self.roomSetting)
        self.window.chatInput.released.connect(self.check)
        self.window.exit.clicked.connect(self.chatEnd)
        ###roompage
        self.window.searchRoom.clicked.connect(self.clickSearch)#searchbar is pressed by mouse
        self.window.searchRoom.released.connect(self.searchRoom)#press enter to search room
        self.window.goRight.clicked.connect(self.rightPage)#roomlist nextpage
        self.window.goLeft.clicked.connect(self.leftPage)#roomlist prevpage
        self.window.addRoom.clicked.connect(self.makeRoom)
        # self.window.mainUserInfo.clicked.connect(self.userinfo)
        self.window.refreshButton.clicked.connect(self.refresh)
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
        self.sign.makingRoom.connect(self.chatStart)
        ##roombtn
        self.roomIndex = roomButtons(self.window)
        self.roomIndex1 = roomButtons(self.window)
        self.roomIndex2 = roomButtons(self.window)
        self.roomIndex3 = roomButtons(self.window)
        self.roomIndex4 = roomButtons(self.window)
        self.roomIndex5 = roomButtons(self.window)
        self.roomIndex.addWid(1,2)
        self.roomIndex1.addWid(2,2)
        self.roomIndex2.addWid(3,2)
        self.roomIndex3.addWid(1,3)
        self.roomIndex4.addWid(2,3)
        self.roomIndex5.addWid(3,3)
        self.roomIndex.room_2.clicked.connect(self.nonhostChatStart)
        self.roomIndex1.room_2.clicked.connect(self.nonhostChatStart)
        self.roomIndex2.room_2.clicked.connect(self.nonhostChatStart)
        self.roomIndex3.room_2.clicked.connect(self.nonhostChatStart)
        self.roomIndex4.room_2.clicked.connect(self.nonhostChatStart)
        self.roomIndex5.room_2.clicked.connect(self.nonhostChatStart)
    
    def chatEnd(self):
        self.window.stackedWidget.setCurrentIndex(1)
        self.player.getCommend("/////종료/////", self.ishost)

    def nonhostChatStart(self):
        self.window.stackedWidget.setCurrentIndex(2)
        self.ishost = False
        self.client = chatClient.chat_Client(self.window, self.id, Gui, sign, self.ishost)
        self.client.start()
        self.player = streamPlayer(self.window, self.client)
        self.player.start()
        self.client.sendPlayerData(self.id+"님이 입장하셨습니다.")
        self.window.chatInput.width()/3*2
    
    
    def setText(self, text):
        pass
    
    def check(self):
        self.client.checker = True

    def chatStart(self):
        self.window.stackedWidget.setCurrentIndex(2)
        self.ishost = True
        self.client = chatClient.chat_Client(self.window, self.id, Gui, sign, self.ishost)
        self.client.start()
        self.player = streamPlayer(self.window, self.client)
        self.player.start()
        self.client.sendPlayerData(self.id+"님이 입장하셨습니다.")

    def getText(self, text, host):
        self.ishost = host
        self.chatText = text
        self.window.chatInput.clear()

    def writeUserChat(self):
        self.player.getCommend(self.chatText, self.ishost)
        self.userChatList.append(userChat(self.window))
        self.userChatList[-1].addWid(self.chatText, self.chatCount)
        self.chatCount += 1
        
    def writeMyChat(self):
        self.player.getCommend(self.chatText, self.ishost)##youtubeplayer get commend
        self.myChatList.append(myChat(self.window))
        self.myChatList[-1].addWid(self.chatText, self.chatCount)
        self.chatCount += 1

    def roomSetting(self):
        roomSettingGUI.gui##set roomsetting
        roomSettingGUI.show(self.window)

    def updateMainWindow(self):
        pass
        ##set all db element

    def login(self):
        self.id = str(self.window.inputid.text())
        pw = str(self.window.inputpw.text())
        
        cursor.execute("SELECT * FROM member WHERE id = %s", (self.id, ))
        data = cursor.fetchall()
        if data == ():
            QtWidgets.QMessageBox.information(self.window.signin, "알림", "존재하지 않는 id 입니다")
            return 0
        if data[0][2] != pw:
            QtWidgets.QMessageBox.information(self.window.signin, "알림", "pw 오류")
            return 0
        self.setPage(False, '')
        self.window.stackedWidget.setCurrentIndex(1)

    def maxiCount(self):
        if self.maxi == False:
            MainWindow.showMaximized()
            self.maxi = True
        elif self.maxi == True:
            MainWindow.showNormal()
            self.maxi = False

    def userinfo(self):
        editUserInfoGUI.show(self.window)
        
    def makeRoom(self):
        roomAddGUI.show(self.sign)##open roomAdd

    def clickSearch(self):
        if (self.window.stackedWidget.currentIndex() != 1):
            pass
        elif (self.window.searchRoom.text() != "검색"):
            pass
        else:
            self.window.searchRoom.clear()

    def searchRoom(self):
        key = self.window.searchRoom.text()
        cursor.execute("SELECT * FROM room WHERE title LIKE %s", ("%" + key + "%",))
        data = cursor.fetchall()
        self.setPage(True, data)

    def setPage(self, search, searchlist):   # 마지막 페이지가 첫 페이지가 아니라면 ...
        if search == True:
            self.data = searchlist
            if self.data == ():
                self.roomIndex.hideWid()
                self.roomIndex1.hideWid()
                self.roomIndex2.hideWid()
                self.roomIndex3.hideWid()
                self.roomIndex4.hideWid()
                self.roomIndex5.hideWid()
                return 0
        else:
            con.autocommit(True)
            cursor.execute("SELECT * FROM room")
            data = cursor.fetchall()
            if data == self.data:
                return 0
            self.data = data
        self.maxPage = (len(self.data) // 6 ) + 1
        self.dataNumRest = len(self.data) % 6 

        if self.maxPage > 1 or (self.maxPage == 1 and self.dataNumRest == 6):
            self.roomIndex.showWid(self.data[0][1], self.data[0][5], self.data[0][7])
            self.roomIndex1.showWid(self.data[1][1], self.data[1][5], self.data[1][7])
            self.roomIndex2.showWid(self.data[2][1], self.data[2][5], self.data[2][7])
            self.roomIndex3.showWid(self.data[3][1], self.data[3][5], self.data[3][7])
            self.roomIndex4.showWid(self.data[4][1], self.data[4][5], self.data[4][7])
            self.roomIndex5.showWid(self.data[5][1], self.data[5][5], self.data[5][7])
        else :
            if self.dataNumRest == 1:
                self.roomIndex.showWid(self.data[0][1], self.data[0][5], self.data[0][7])
            elif self.dataNumRest == 2:
                self.roomIndex.showWid(self.data[0][1], self.data[0][5], self.data[0][7])
                self.roomIndex1.showWid(self.data[1][1], self.data[1][5], self.data[1][7])
            elif self.dataNumRest == 3:
                self.roomIndex.showWid(self.data[0][1], self.data[0][5], self.data[0][7])
                self.roomIndex1.showWid(self.data[1][1], self.data[1][5], self.data[1][7])
                self.roomIndex2.showWid(self.data[2][1], self.data[2][5], self.data[2][7])
            elif self.dataNumRest == 4:
                self.roomIndex.showWid(self.data[0][1], self.data[0][5], self.data[0][7])
                self.roomIndex1.showWid(self.data[1][1], self.data[1][5], self.data[1][7])
                self.roomIndex2.showWid(self.data[2][1], self.data[2][5], self.data[2][7])
                self.roomIndex3.showWid(self.data[3][1], self.data[3][5], self.data[3][7])
            elif self.dataNumRest == 5:
                self.roomIndex.showWid(self.data[0][1], self.data[0][5], self.data[0][7])
                self.roomIndex1.showWid(self.data[1][1], self.data[1][5], self.data[1][7])
                self.roomIndex2.showWid(self.data[2][1], self.data[2][5], self.data[2][7])
                self.roomIndex3.showWid(self.data[3][1], self.data[3][5], self.data[3][7])
                self.roomIndex4.showWid(self.data[4][1], self.data[4][5], self.data[4][7])
    # 새로고침 버튼을 눌렀을 때의 이벤트 처리
    def refresh(self):
        self.pageNum = 1  
        self.startIndex = 0
        self.maxPage = 1  
        self.dataNumRest = 0   
        self.setPage(False, ())     

    def setWid(self, data):
        if self.dataNumRest == 1:
            self.roomIndex.showWid(data[self.startIndex][1], data[self.startIndex][5], data[self.startIndex][7])
            self.roomIndex1.hideWid()
            self.roomIndex2.hideWid()
            self.roomIndex3.hideWid()
            self.roomIndex4.hideWid()
            self.roomIndex5.hideWid()
        elif self.dataNumRest == 2:
            self.roomIndex.showWid(data[self.startIndex][1], data[self.startIndex][5], data[self.startIndex][7])
            self.roomIndex1.showWid(data[self.startIndex+1][1], data[self.startIndex+1][5], data[self.startIndex+1][7])
            self.roomIndex2.hideWid()
            self.roomIndex3.hideWid()
            self.roomIndex4.hideWid()
            self.roomIndex5.hideWid()
        elif self.dataNumRest == 3:
            self.roomIndex.showWid(data[self.startIndex][1], data[self.startIndex][5], data[self.startIndex][7])
            self.roomIndex1.showWid(data[self.startIndex+1][1], data[self.startIndex+1][5], data[self.startIndex+1][7])
            self.roomIndex2.showWid(data[self.startIndex+2][1], data[self.startIndex+2][5], data[self.startIndex+2][7])
            self.roomIndex3.hideWid()
            self.roomIndex4.hideWid()
            self.roomIndex5.hideWid()
        elif self.dataNumRest == 4:
            self.roomIndex.showWid(data[self.startIndex][1], data[self.startIndex][5], data[self.startIndex][7])
            self.roomIndex1.showWid(data[self.startIndex+1][1], data[self.startIndex+1][5], data[self.startIndex+1][7])
            self.roomIndex2.showWid(data[self.startIndex+2][1], data[self.startIndex+2][5], data[self.startIndex+2][7])
            self.roomIndex3.showWid(data[self.startIndex+3][1], data[self.startIndex+3][5], data[self.startIndex+3][7])
            self.roomIndex4.hideWid()
            self.roomIndex5.hideWid()
        elif self.dataNumRest == 5:
            self.roomIndex.showWid(data[self.startIndex][1], data[self.startIndex][5], data[self.startIndex][7])
            self.roomIndex1.showWid(data[self.startIndex+1][1], data[self.startIndex+1][5], data[self.startIndex+1][7])
            self.roomIndex2.showWid(data[self.startIndex+2][1], data[self.startIndex+2][5], data[self.startIndex+2][7])
            self.roomIndex3.showWid(data[self.startIndex+3][1], data[self.startIndex+3][5], data[self.startIndex+3][7])
            self.roomIndex4.showWid(data[self.startIndex+4][1], data[self.startIndex+4][5], data[self.startIndex+4][7])
            self.roomIndex5.hideWid()
        elif self.dataNumRest == 0:
            self.roomIndex.showWid(data[self.startIndex][1], data[self.startIndex][5], data[self.startIndex][7])
            self.roomIndex1.showWid(data[self.startIndex+1][1], data[self.startIndex+1][5], data[self.startIndex+1][7])
            self.roomIndex2.showWid(data[self.startIndex+2][1], data[self.startIndex+2][5], data[self.startIndex+2][7])
            self.roomIndex3.showWid(data[self.startIndex+3][1], data[self.startIndex+3][5], data[self.startIndex+3][7])
            self.roomIndex4.showWid(data[self.startIndex+4][1], data[self.startIndex+4][5], data[self.startIndex+4][7])
            self.roomIndex5.showWid(data[self.startIndex+5][1], data[self.startIndex+5][5], data[self.startIndex+5][7])

    def rightPage(self):
        if self.pageNum != self.maxPage:   # 마지막 페이지가 아니라면, 아래 내용을 동작시킴

            self.pageNum += 1   # 페이지 1 증가
            self.startIndex = 6 * (self.pageNum - 1)   # 페이지가 변경되었기 때문에, 시작 index값을 변경시킴
               # 이동 후 내 위치가 마지막 페이지가 아니라면 ...
            self.setWid(self.data)     # 마지막 페이지가 아니라면 무조건 6개의 값이 출력될 것이기 때문에

    def leftPage(self):
        if self.pageNum != 1:   # 첫 번째 페이지가 아니라면, 아래 내용을 동작시킴

            self.pageNum -= 1   # 페이지 1 감소
            self.startIndex = 6 * (self.pageNum-1)   # 페이지가 변경되었기 때문에, 시작 index값을 변경시킴
            
            if self.pageNum < self.maxPage:# 왼쪽으로 이동은 무조건 6개가 채워져있을 것이기 때문에 아래 내용만 정의하면 됨
                self.roomIndex.showWid(self.data[self.startIndex][1], self.data[self.startIndex][6], self.data[self.startIndex][7])
                self.roomIndex1.showWid(self.data[self.startIndex+1][1], self.data[self.startIndex+1][6], self.data[self.startIndex+1][7])
                self.roomIndex2.showWid(self.data[self.startIndex+2][1], self.data[self.startIndex+2][6], self.data[self.startIndex+2][7])
                self.roomIndex3.showWid(self.data[self.startIndex+3][1], self.data[self.startIndex+3][6], self.data[self.startIndex+3][7])
                self.roomIndex4.showWid(self.data[self.startIndex+4][1], self.data[self.startIndex+4][6], self.data[self.startIndex+4][7])
                self.roomIndex5.showWid(self.data[self.startIndex+5][1], self.data[self.startIndex+5][6], self.data[self.startIndex+5][7])

if __name__=="__main__":
    sign = mainWindow.sig()

    con = pymysql.connect(
        user = 'IGRUS',

        password = 'igrus1234',
        host = '13.124.126.150',
        db = 'ICBM',
        charset= 'utf8'
    )
    cursor = con.cursor()

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
    
    sys.exit(app.exec_())