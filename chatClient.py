from PyQt5 import QtCore, QtGui, QtWidgets
import mainWindowGUI, userChat
import socket
import argparse
import threading
import time
#접속하고 싶은 ip와 port를 입력받는 클라이언트 코드를 작성해보자.
# 접속하고 싶은 포트를 입력한다.
class chat_Client(threading.Thread):
    def __init__(self, ui, userName, main, sign, ishost):
        threading.Thread.__init__(self)
        self.gui = main
        self.window = ui
        self.port = 4000
        self.host = "13.124.126.150"
        # self.host = "127.0.0.1"
        self.user = userName
        self.checker = False
        self.sign = sign
        self.hostcheck = ishost

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        self.client_socket.send(self.user.encode('utf-8'))

        
    def run(self):
        receive_thread = threading.Thread(target=self.handle_receive, args=(self.client_socket, self.user))
        receive_thread.daemon = True
        receive_thread.start()

        send_thread = threading.Thread(target=self.handle_send, args=(self.client_socket,))
        send_thread.daemon = True
        send_thread.start()

        send_thread.join()
        receive_thread.join()

        while True:
            if self.port == 1:
                break

    def handle_receive(self, client_socket, user):
        while 1:
            try:
                data = client_socket.recv(1024)
            except:
                print("연결 끊김")
                break
            data = data.decode('utf-8')
            if not user in data:
                self.gui.getText(data, self.hostcheck)
                self.sign.user()
                # self.gui.writeUserChat(data)#유저가 친 채팅일 경우
                # self.chatui.chat.setText(self.data)
                # self.window.chatArea.addWidget(self.chatui)

    def getText(self):
        text = self.window.chatInput.text()
        return text
    
    def sendPlayerData(self, data):
        self.client_socket.send(str(data).encode('utf-8'))
        self.gui.getText(str(data), self.hostcheck)
        self.sign.my()
        
    def handle_send(self, client_socket):
        while 1:
            if self.checker == True:
                self.checker = False
                text = self.getText()
                client_socket.send(text.encode('utf-8'))
                if text == "/종료":
                    break
                else:
                    self.gui.getText(text, self.hostcheck)
                    self.sign.my()
                    #self.gui.writeMyChat(self.input_text)#내가 친 채팅일 경우
               

        client_socket.close()