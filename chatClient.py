import mainWindowGUI, userChat
import socket
import argparse
import threading
import time

#접속하고 싶은 ip와 port를 입력받는 클라이언트 코드를 작성해보자.
# 접속하고 싶은 포트를 입력한다.
class chat_Client(threading.Thread):
    def __init__(self, ui, userName, win):
        threading.Thread.__init__(self)
        print("init")

        self.func = win
        self.window = ui
        self.port = 4000
        self.host = "13.124.126.150"
        self.user = userName
        self.input_text = ""

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
                self.data = client_socket.recv(1024)
            except:
                print("연결 끊김")
                break
            self.data = self.data.decode('utf-8')
            if not user in self.data:
                print(self.data)
                # self.chatui.chat.setText(self.data)
                # self.window.chatArea.addWidget(self.chatui)

    def getText(self):
        self.input_text = self.window.chatInput.text()

    def handle_send(self, client_socket):
        while 1:
            self.window.chatInput.released.connect(self.getText)
            print(self.input_text)
            ##self.data = input()
            client_socket.send(self.input_text.encode('utf-8'))
            if self.input_text == "/종료":
                break
            else:
                self.func.writeChat(self.input_text)
               

        client_socket.close()


        
    #parser와 관련된 메서드 정리된 블로그 : https://docs.python.org/ko/3/library/argparse.html
    #description - 인자 도움말 전에 표시할 텍스트 (기본값: none)
    #help - 인자가 하는 일에 대한 간단한 설명.
    #nargs - 소비되어야 하는 명령행 인자의 수. -> '+'로 설정 시 모든 명령행 인자를 리스트로 모음 + 없으면 경고
    #required - 명령행 옵션을 생략 할 수 있는지 아닌지 (선택적일 때만).
    # parser = argparse.ArgumentParser(description="\nJoo's client\n-p \n-i host\n-s string")
    # parser.add_argument('-p', help="port")
    # parser.add_argument('-i', help="host", required=True)
    # parser.add_argument('-u', help="user", required=True)

    # args = parser.parse_args()
    # host = args.i
    # user = str(args.u)
    # try:
    #     port = int(args.p)
    # except:
    #     pass