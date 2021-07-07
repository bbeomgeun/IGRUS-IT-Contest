from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import threading
import random
import pafy
from timer import timer, checker
import string
import pymysql
import sys, os


class streamPlayer(threading.Thread):
        def __init__(self, window, client):
                threading.Thread.__init__(self)
                self.commend = ''
                self.keyword = ''
                self.searchPage = ''
                self.playPage = ''
                self.playlist = []
                self.volume = 100
                self.nowPlay = ''
                self.nowUrl = ''
                self.wait = ''
                self.window = window
                self.check = False
                self.timer = ''
                self.checker = ''
                self.con = ''
                self.cursor = ''
                self.idx = 0
                self.client = client
                self.ishost = False

        def chooseCommend(self, comm):
                if comm == '':
                        return 0
                commend = comm.split()
                commend[0] = commend[0].lower()
                if commend[0].isdecimal() == True and int(commend[0]) > 0 and int(commend[0]) <= 5:
                        self.addQueue(int(commend[0]))
                elif commend[0] == "search":
                        try:
                                self.keyword = commend[1]
                        except:
                                return 0
                        self.searchMusic()
                elif commend[0] == 'queue':
                        print(self.playlist)
                elif commend[0] == 'delete':
                        try:
                                num = commend[1]
                        except:
                                return 0
                        del self.playlist[num]
                elif commend[0] == 'repeat':
                        self.playlist.insert(0, (self.nowPlay, self.nowUrl))
                elif commend[0] == 'shuffle':
                        random.shuffle(self.playlist)
                elif commend[0] == 'purge':
                        self.playlist = []
                else:
                        self.musicControl(commend)
        def searchMusic(self):
                ##get keyword
                baseUrl = "https://www.youtube.com/results?search_query={}".format(self.keyword)
                option = webdriver.ChromeOptions()
                option.add_argument("headless")
                # chromeDriverPath = "D:/Desktop/PYQT/IGRUS_Contest_2020/chromedriver.exe"
                # self.searchPage = webdriver.Chrome(chromeDriverPath, options = option)
                
                if  getattr(sys, 'frozen', False): 
                        chromedriver_path = os.path.join(sys, '_MEIPASS', "chromedriver.exe")
                        self.searchPage = webdriver.Chrome(chromedriver_path, options = option)
                else:
                        self.searchPage = webdriver.Chrome("C:/Users/sec/chromedriver.exe", options = option)
                self.searchPage.get(baseUrl)
                self.wait = WebDriverWait(self.searchPage, 10)
                self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a > yt-formatted-string")))
                soup = BeautifulSoup(self.searchPage.page_source, "html.parser")
                title = soup.select("a > yt-formatted-string")
                titleList = []
                for i in range (5):
                        titleList.append(title[i].text)
                self.client.sendPlayerData(titleList)

        def addQueue(self, num):
                if (num == 0): return 0
                self.searchPage.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{}]/div[1]/div/div[1]/div/h3/a/yt-formatted-string".format(num)).click()
                self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ytd-compact-video-renderer > div > div > div > a > h3 > span")))
                url = str(self.searchPage.current_url)
                soup = BeautifulSoup(self.searchPage.page_source, "html.parser")
                title = str(soup.select("ytd-video-primary-info-renderer > div > h1 > yt-formatted-string")[0].text)
                self.searchPage.close()
                self.playlist.append((title, url))
                # self.cursor.execute("UPDATE room SET playList=%s WHERE idx=%s", (str(self.playlist), self.idx))
                # self.con.commit()
                self.playMusic()

        def playMusic(self):
                if len(self.playlist) == 0:
                        return 0
                if self.checker != '':
                        if self.checker.check == False:
                                return 0
                # self.cursor.execute("SELECT (playList) FROM room WHERE idx=%s", (self.idx, ))
                # play = list(self.cursor.fetchall()[0])
                now = self.playlist.pop(0)
                self.nowPlay = now[0]
                self.window.songInfo.setText("now Playing - " + str(self.nowPlay))
                url = now[1]
                video = pafy.new(url)
                bestAudio = video.getbestaudio()
                length = video.duration
                length = length.split(":")
                length = int(length[0])*60*60 + int(length[1])*60 + int(length[2])
                
                audioUrl = str(bestAudio.url)
                option = webdriver.ChromeOptions()
                option.add_argument("headless")
                # chromeDriverPath = "D:/Desktop/PYQT/IGRUS_Contest_2020/chromedriver.exe"
                # self.playPage = webdriver.Chrome(chromeDriverPath, options = option)
                if  getattr(sys, 'frozen', False): 
                        chromedriver_path = os.path.join(sys, '_MEIPASS', "chromedriver.exe")
                        self.playPage = webdriver.Chrome(chromedriver_path, options = option)
                else:
                        self.playPage = webdriver.Chrome("C:/Users/sec/chromedriver.exe", options = option)
                self.playPage.get(audioUrl)
                self.timer = timer(length)
                self.checker = checker(self.timer)
                self.timer.start()
                self.checker.start()

        def musicControl(self, commend):
                commend = commend[0].lower()
                if commend[0] == 'volume':
                        try:
                                volume =  commend[1]
                        except:
                                return 0

                        for i in range (3):
                                self.playPage.find_element_by_xpath("/html/body").send_keys(Keys.TAB)
                        if self.volume > volume:
                                for i in range (self.volume - volume):
                                        self.playPage.find_element_by_xpath("/html/body/video").send_keys(Keys.ARROW_LEFT)
                                self.playPage.find_element_by_xpath("/html/body").click()
                        elif volume == 100:
                                self.playPage.find_element_by_xpath("/html/body/video").send_keys(Keys.HOME)
                                self.playPage.find_element_by_xpath("/html/body").click()
                        elif volume == 0 or volume.lower() == "mute":
                                self.playPage.find_element_by_xpath("/html/body/video").send_keys(Keys.END)
                                self.playPage.find_element_by_xpath("/html/body").click()        
                        else :
                                for i in range (volume - self.volume):
                                        self.playPage.find_element_by_xpath("/html/body/video").send_keys(Keys.ARROW_RIGHT)
                                self.playPage.find_element_by_xpath("/html/body").click()
                        self.volume = volume
                elif commend == 'skip':
                        self.timer.skip = True
                elif commend == 'pause':
                        self.playPage.find_element_by_xpath("/html/body").send_keys(Keys.SPACE)
                        if self.timer.pause == True:
                                self.timer.pauseEvent.set()
                                self.timer.pause = False
                        elif self.timer.pause == False:
                                self.timer.pause = True
                else:
                        return 0

        def getCommend(self, data, host):
                self.ishost = host
                self.commend = data
                self.check = True

        def run(self):
                self.con = pymysql.connect(
                user = 'IGRUS',
                password = 'igrus1234',
                host = '13.124.126.150',
                db = 'ICBM',
                charset= 'utf8'
                )
                self.cursor = self.con.cursor()
                self.idx = 1

                while True:
                        if self.check:##get commend
                                self.check = False
                                if self.commend == "/////종료/////":
                                        break
                                self.chooseCommend(self.commend)
                        if self.checker != '':
                                if self.checker.check == True:##1곡 끝난거 체크되면 다음곡 재생
                                        self.checker.checkWait.set()
                                        self.playPage.close()
                                        self.playMusic()
                                if self.checker.skip == True:
                                        self.playPage.close()
                                        self.playMusic()

                
                        

    # def youtube(self):
    #     url = "https://www.youtube.com/watch?v=PqM"
    #     video = pafy.new(url)
    #     bestAudio = video.getbestaudio()
    #     length = video.duration
    #     length = length.split(":")
    #     audioUrl = str(bestAudio.url)
    #     option = webdriver.ChromeOptions()
    #     # option.add_argument("headless")
    #     chromeDriverPath = "D:/Desktop/chromedriver.exe"
    #     self.driver = webdriver.Chrome(chromeDriverPath, options = option)

    # # def pause(self):
    # #     self.driver.find_element_by_xpath("/html/body/video/source").send_keys(Keys.SPACE)

    #     self.driver.get(audioUrl)