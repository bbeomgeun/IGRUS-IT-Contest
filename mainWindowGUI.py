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


        self.pageNum = 1   # 현재 페이지 지정
        self.startIndex = 6 * (self.pageNum - 1)   # 각 페이지에서 데이터베이스 값의 시작 인덱스 지정
                                                   # index[0][1]은 첫 번째 row의 첫번째 column 값을 의미 (column 중 id는 식별자이기 때문에 무시됨)
        self.maxPage = 1   # 데이터 개수에 따라 마지막 페이지 지정
        self.dataNumRest = 0   # 마지막 페이지에 존재하는 데이터의 개수


        ###loginpage
        self.window.join.clicked.connect(lambda: joinUserGUI.show())
        self.window.signin.clicked.connect(self.login)
        self.window.inputpw.setEchoMode(2)
        ###chatpage
        self.window.chatUserInfo.clicked.connect(self.userinfoSetting)
        self.window.chatRoomTitle.clicked.connect(lambda: roomSettingGUI.show(self.window.chatRoomTitle.text()))
        self.window.chatInput.released.connect(self.check)
        #self.window.exit.clicked.connect(
        ###roompage
        self.window.searchRoom.clicked.connect(self.clickSearch)#searchbar is pressed by mouse
        self.window.searchRoom.released.connect(self.searchRoom)#press enter to search room
        self.window.goRight.clicked.connect(self.rightPage)#roomlist nextpage
        self.window.goLeft.clicked.connect(self.leftPage)#roomlist prevpage
        self.window.addRoom.clicked.connect(self.makeRoom)
        self.window.mainUserInfo.clicked.connect(lambda: editUserInfoGUI.show(self.window))
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
        ##makeroombtn
        
    def check(self):
        self.client.checker = True

    def chatStart(self):
        self.window.stackedWidget.setCurrentIndex(2)
        self.ishost = True
        self.client = chatClient.chat_Client(self.window, "범근", Gui, sign, self.ishost)
        self.client.start()
        self.player = streamPlayer(self.window, self.client)
        self.player.start()

    def getText(self, text, host):
        self.ishost = host
        self.chatText = text
        self.window.chatInput.clear()

    def writeUserChat(self):
        self.player.getCommend(self.chatText, self.ishost)
        self.userChatList.append(userChat(self.window))
        self.userChatList[self.chatCount].addWid(self.chatText, self.chatCount)
        self.chatCount += 1
        
    def writeMyChat(self):
        self.player.getCommend(self.chatText, self.ishost)##youtubeplayer get commend
        self.myChatList.append(myChat(self.window))
        self.myChatList[self.chatCount].addWid(self.chatText, self.chatCount)
        self.chatCount += 1

    def userinfoSetting(self):
        roomSettingGUI.gui##set roomsetting
        roomSettingGUI.show(self.window)

    def updateMainWindow(self):
        pass
        ##set all db element

    def login(self):
        self.roomIndex = roomButtons(self.window)
        self.roomIndex1 = roomButtons(self.window)
        self.roomIndex2 = roomButtons(self.window)
        self.roomIndex3 = roomButtons(self.window)
        self.roomIndex4 = roomButtons(self.window)
        self.roomIndex5 = roomButtons(self.window)
        id = str(self.window.inputid.text())
        pw = str(self.window.inputpw.text())
        
        cursor.execute("SELECT * FROM member WHERE id = %s", (id, ))
        data = cursor.fetchall()
        if data == ():
            QtWidgets.QMessageBox.information(self.window.signin, "알림", "존재하지 않는 id 입니다")
            return 0
        if data[0][2] != pw:
            QtWidgets.QMessageBox.information(self.window.signin, "알림", "pw 오류")
            return 0
        self.setPage()
        self.window.stackedWidget.setCurrentIndex(1)

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
        roomAddGUI.show(self.sign)##open roomAdd

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


    def setPage(self):
        sql = "SELECT * FROM room;"
        cursor.execute(sql)
        data = cursor.fetchall()
        self.maxPage = (len(data) // 6 ) + 1
        self.dataNumRest = len(data) % 6 

        if self.maxPage > 1:   # 마지막 페이지가 첫 페이지가 아니라면 ...
            self.roomIndex.addWid(data[0][1], data[0][5], data[0][7], 1,2)
            self.roomIndex1.addWid(data[1][1], data[1][5], data[1][7], 2,2)
            self.roomIndex2.addWid(data[2][1], data[2][5], data[2][7], 3,2)
            self.roomIndex3.addWid(data[3][1], data[3][5], data[3][7], 1,3)
            self.roomIndex4.addWid(data[4][1], data[4][5], data[4][7], 2,3)
            self.roomIndex5.addWid(data[5][1], data[5][5], data[5][7], 3,3)
        else :
            if self.dataNumRest == 1:
                self.roomIndex.addWid(data[0][1], data[0][5], data[0][7], 1,2)
            elif self.dataNumRest == 2:
                self.roomIndex.addWid(data[0][1], data[0][5], data[0][7], 1,2)
                self.roomIndex1.addWid(data[1][1], data[1][5], data[1][7], 2,2)
            elif self.dataNumRest == 3:
                self.roomIndex.addWid(data[0][1], data[0][5], data[0][7], 1,2)
                self.roomIndex1.addWid(data[1][1], data[1][5], data[1][7], 2,2)
                self.roomIndex2.addWid(data[2][1], data[2][5], data[2][7], 3,2)
            elif self.dataNumRest == 4:
                self.roomIndex.addWid(data[0][1], data[0][5], data[0][7], 1,2)
                self.roomIndex1.addWid(data[1][1], data[1][5], data[1][7], 2,2)
                self.roomIndex2.addWid(data[2][1], data[2][5], data[2][7], 3,2)
                self.roomIndex3.addWid(data[3][1], data[3][5], data[3][7], 1,3)
            elif self.dataNumRest == 5:
                self.roomIndex.addWid(data[0][1], data[0][5], data[0][7], 1,2)
                self.roomIndex1.addWid(data[1][1], data[1][5], data[1][7], 2,2)
                self.roomIndex2.addWid(data[2][1], data[2][5], data[2][7], 3,2)
                self.roomIndex3.addWid(data[3][1], data[3][5], data[3][7], 1,3)
                self.roomIndex4.addWid(data[4][1], data[4][5], data[4][7], 2,3)
            elif self.dataNumRest == 6:
                self.roomIndex.addWid(data[0][1], data[0][5], data[0][7], 1,2)
                self.roomIndex1.addWid(data[1][1], data[1][5], data[1][7], 2,2)
                self.roomIndex2.addWid(data[2][1], data[2][5], data[2][7], 3,2)
                self.roomIndex3.addWid(data[3][1], data[3][5], data[3][7], 1,3)
                self.roomIndex4.addWid(data[4][1], data[4][5], data[4][7], 2,3)
                self.roomIndex5.addWid(data[5][1], data[5][5], data[5][7], 3,3)

    # 새로고침 버튼을 눌렀을 때의 이벤트 처리
    def refresh(self):
        sql = "SELECT * FROM room;"
        cursor.execute(sql)
        data = cursor.fetchall()
        self.maxPage = (len(data) // 6 ) + 1
        self.dataNumRest = len(data) % 6 

        if self.pageNum == self.maxPage:   # 현재 페이지가 마지막 페이지라면...
            self.setWid(data)      
                            # 왜냐하면, 한 페이지에 값이 6개 미만으로 들어가는 경우는 마지막 페이지밖에 없기 때문에
    def setWid(self, data):
        if self.dataNumRest == 1:
            self.roomIndex.addWid(data[self.startIndex][1], data[self.startIndex][5], data[self.startIndex][7], 1,2)
            self.roomIndex1.delWid()
            self.roomIndex2.delWid()
            self.roomIndex3.delWid()
            self.roomIndex4.delWid()
            self.roomIndex5.delWid()
        elif self.dataNumRest == 2:
            self.roomIndex.addWid(data[self.startIndex][1], data[self.startIndex][5], data[self.startIndex][7], 1,2)
            self.roomIndex.addWid(data[self.startIndex+1][1], data[self.startIndex+1][5], data[self.startIndex+1][7], 2,2)
            self.roomIndex2.delWid()
            self.roomIndex3.delWid()
            self.roomIndex4.delWid()
            self.roomIndex5.delWid()
        elif self.dataNumRest == 3:
            self.roomIndex.addWid(data[self.startIndex][1], data[self.startIndex][5], data[self.startIndex][7], 1,2)
            self.roomIndex.addWid(data[self.startIndex+1][1], data[self.startIndex+1][5], data[self.startIndex+1][7], 2,2)
            self.roomIndex.addWid(data[self.startIndex+2][1], data[self.startIndex+2][5], data[self.startIndex+2][7], 3,2)
            self.roomIndex3.delWid()
            self.roomIndex4.delWid()
            self.roomIndex5.delWid()
        elif self.dataNumRest == 4:
            self.roomIndex.addWid(data[self.startIndex][1], data[self.startIndex][5], data[self.startIndex][7], 1,2)
            self.roomIndex.addWid(data[self.startIndex+1][1], data[self.startIndex+1][5], data[self.startIndex+1][7], 2,2)
            self.roomIndex.addWid(data[self.startIndex+2][1], data[self.startIndex+2][5], data[self.startIndex+2][7], 3,2)
            self.roomIndex.addWid(data[self.startIndex+3][1], data[self.startIndex+3][5], data[self.startIndex+3][7], 1,3)
            self.roomIndex4.delWid()
            self.roomIndex5.delWid()
        elif self.dataNumRest == 5:
            self.roomIndex.addWid(data[self.startIndex][1], data[self.startIndex][5], data[self.startIndex][7], 1,2)
            self.roomIndex.addWid(data[self.startIndex+1][1], data[self.startIndex+1][5], data[self.startIndex+1][7], 2,2)
            self.roomIndex.addWid(data[self.startIndex+2][1], data[self.startIndex+2][5], data[self.startIndex+2][7], 3,2)
            self.roomIndex.addWid(data[self.startIndex+3][1], data[self.startIndex+3][5], data[self.startIndex+3][7], 1,3)
            self.roomIndex.addWid(data[self.startIndex+4][1], data[self.startIndex+4][5], data[self.startIndex+4][7], 2,3)
            self.roomIndex5.delWid()
        elif self.dataNumRest == 6:
            self.roomIndex.addWid(data[self.startIndex][1], data[self.startIndex][5], data[self.startIndex][7], 1,2)
            self.roomIndex.addWid(data[self.startIndex+1][1], data[self.startIndex+1][5], data[self.startIndex+1][7], 2,2)
            self.roomIndex.addWid(data[self.startIndex+2][1], data[self.startIndex+2][5], data[self.startIndex+2][7], 3,2)
            self.roomIndex.addWid(data[self.startIndex+3][1], data[self.startIndex+3][5], data[self.startIndex+3][7], 1,3)
            self.roomIndex.addWid(data[self.startIndex+4][1], data[self.startIndex+4][5], data[self.startIndex+4][7], 2,3)
            self.roomIndex.addWid(data[self.startIndex+5][1], data[self.startIndex+5][5], data[self.startIndex+5][7], 3,3)
        else:   # 현재 페이지가 마지막 페이지가 아니라면 ...
                # 마지막 페이지가 아니라면, 6개의 값이 모두 차있을 것이기 때문에
            self.roomIndex.addWid(data[self.startIndex][1], data[self.startIndex][5], data[self.startIndex][7], 1,2)
            self.roomIndex.addWid(data[self.startIndex+1][1], data[self.startIndex+1][5], data[self.startIndex+1][7], 2,2)
            self.roomIndex.addWid(data[self.startIndex+2][1], data[self.startIndex+2][5], data[self.startIndex+2][7], 3,2)
            self.roomIndex.addWid(data[self.startIndex+3][1], data[self.startIndex+3][5], data[self.startIndex+3][7], 1,3)
            self.roomIndex.addWid(data[self.startIndex+4][1], data[self.startIndex+4][5], data[self.startIndex+4][7], 2,3)
            self.roomIndex.addWid(data[self.startIndex+5][1], data[self.startIndex+5][5], data[self.startIndex+5][7], 3,3)

    def rightPage(self):
        sql = "SELECT * FROM room;"
        cursor.execute(sql)
        data = cursor.fetchall()

        if self.pageNum != self.maxPage:   # 마지막 페이지가 아니라면, 아래 내용을 동작시킴

            self.pageNum += 1   # 페이지 1 증가
            self.startIndex = 6 * (self.pageNum - 1)   # 페이지가 변경되었기 때문에, 시작 index값을 변경시킴
            
            if self.pageNum < self.maxPage:   # 이동 후 내 위치가 마지막 페이지가 아니라면 ...
                self.setWid(data)     # 마지막 페이지가 아니라면 무조건 6개의 값이 출력될 것이기 때문에

                
    def leftPage(self):
        sql = "SELECT * FROM room;"
        cursor.execute(sql)
        data = cursor.fetchall()

        if self.pageNum != 1:   # 첫 번째 페이지가 아니라면, 아래 내용을 동작시킴

            self.pageNum -= 1   # 페이지 1 감소
            self.startIndex = 6 * (self.pageNum - 1)   # 페이지가 변경되었기 때문에, 시작 index값을 변경시킴
            
            if self.pageNum < self.maxPage:   # 왼쪽으로 이동은 무조건 6개가 채워져있을 것이기 때문에 아래 내용만 정의하면 됨
                self.roomIndex.addWid(data[self.startIndex][1], data[self.startIndex][6], data[self.startIndex][7], 1,2)
                self.roomIndex.addWid(data[self.startIndex+1][1], data[self.startIndex+1][6], data[self.startIndex+1][7], 2,2)
                self.roomIndex.addWid(data[self.startIndex+2][1], data[self.startIndex+2][6], data[self.startIndex+2][7], 3,2)
                self.roomIndex.addWid(data[self.startIndex+3][1], data[self.startIndex+3][6], data[self.startIndex+3][7], 1,3)
                self.roomIndex.addWid(data[self.startIndex+4][1], data[self.startIndex+4][6], data[self.startIndex+4][7], 2,3)
                self.roomIndex.addWid(data[self.startIndex+5][1], data[self.startIndex+5][6], data[self.startIndex+5][7], 3,3)

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