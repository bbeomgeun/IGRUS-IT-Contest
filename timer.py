import threading
import time

class timer(threading.Thread):
    def __init__(self, length):
        threading.Thread.__init__(self)
        self.length = length
        self.time = ''
        self.pause = False
        self.pauseEvent = threading.Event()
        self.skip = False

    def run(self):
        self.time = time.time()
        while True:
            if time.time() - self.time > self.length + 1:
                break
            if self.skip == True:
                break
            if self.pause == True:
                pauseTime = time.time()
                self.pauseEvent.wait()
                self.pause = False
                Time = time.time() - pauseTime
                self.time += Time
                self.pauseEvent.clear()


class checker(threading.Thread):
        def __init__(self, timer):
                threading.Thread.__init__(self)
                self.timer = timer
                self.check = False
                self.skip = False
                self.checkWait = threading.Event()

        def run(self):
                while True:
                    if not self.timer.is_alive():
                        self.check = True
                        self.checkWait.wait()
                        break
                    if self.timer.skip == True:
                        self.skip = True
                        self.timer.pauseEvent.set()
                        break
        