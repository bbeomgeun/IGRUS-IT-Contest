import mainWindow, roomButton
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class GUI:
    def __init__(self, ui):
        self.window = ui
        self.roomPage = 1#current roomlist page
        self.window.searchRoom.clicked.connect(self.clickSearch)#searchbar is pressed by mouse
        self.window.searchRoom.released.connect(self.searchRoom)#press enter to search room
        self.window.goRight.clicked.connect(lambda: self.goPage(True))#roomlist nextpage
        self.window.goLeft.clicked.connect(lambda: self.goPage(False))#roomlist prevpage

    def goPage(self, change):
        roomNum = 1#testval
        #get roomnum, roomcount from db
        if (change == True):#goRight
            if self.roomPage <= roomNum/6 and roomNum/6 != 0:
                #get roominfo from db
                pass

        elif (change == False):#goLeft
            if self.roomPage <= 1:
                #get roominfo from db
                pass

    def clickSearch(self):
        if (self.window.stackedWidget.currentIndex() != 1):
            pass
        elif (self.window.searchRoom.text() != "검색"):
            pass
        else:
            self.window.searchRoom.clear()

    def searchRoom(self):
        #get roominfo from db
        print("search")#enter test
        #infolist->각 요소별로 room객체에 뿌려줌
        pass
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainWindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    Gui = GUI(ui)
    sys.exit(app.exec_())