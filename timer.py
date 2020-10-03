import threading
import time

class timer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        