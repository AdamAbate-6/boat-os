import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1)
import pigpio

class SpeedController:

    def __init__(self, runSpeed):
        # GPIO pin controlling ESC = 4.
        self.ESC = 4
        
        self.pi = pigpio.pi()
        self.pi.baudrate = 9600
        
        self.runSpeed = runSpeed

    def armESC(self):	
        self.pi.set_servo_pulsewidth(self.ESC, 0)
        print("turn on battery, wait five seconds")
        time.sleep(5)
        self.pi.set_servo_pulsewidth(self.ESC, 700)
        print("wait again ha ha")
        time.sleep(3)

    def runESC(self):	
        self.pi.set_servo_pulsewidth(self.ESC, self.runSpeed)
		
    def setSpeed(self, newSpeed):
        self.runSpeed = newSpeed
    
