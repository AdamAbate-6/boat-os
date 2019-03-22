import threading
import time

class MotorController(threading.Thread):

    def __init__(self, delay):
        self.delay = delay
        threading.Thread.__init__(self)
    
    def run(self):
        while 1:
            print("MC Thread: Controlling motors")
            time.sleep(self.delay)