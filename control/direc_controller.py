# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
# Modified by Adam Abate and Simon Hetzler in 2018 and 2019
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

import numpy as np


class DirectionController:

    def __init__(self):
        # Initialise the PCA9685 using the default address (0x40).
        self.pwm = Adafruit_PCA9685.PCA9685()

        # Alternatively specify a different address and/or bus:
        #pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

        # Configure min and max servo pulse lengths
        self.absolute_servo_min = 150  # Min pulse length out of 4096
        self.servo_max = 411 #corresponds to VSD range of motion
        self.servo_center = 375 #puts servo half way between minimums and maximums
        self.servo_min = 339 #corresponds to VSD range of motion
        self.absolute_servo_max = 600  # Max pulse length out of 4096

        # Set frequency to 60hz, good for servos.
        self.pwm.set_pwm_freq(60)
    
    # Helper function to make setting a servo pulse width simpler.
    def setServoPulse(self, channel, pulse):
        pulse_length = 1000000    # 1,000,000 us per second
        pulse_length //= 60       # 60 Hz
        print('{0}us per period'.format(pulse_length))
        pulse_length //= 4096     # 12 bits of resolution
        print('{0}us per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        self.pwm.set_pwm(channel, 0, pulse)
    
    def adjustServos(self, newDirec):

        # Convert input to Numpy array.
        newDirec = np.array(newDirec)

        # We need to detect if all direction vector elements are zero -- see if-else below.
        allzeros = False
        for i in range(0,3):
            if (newDirec[i] != 0):
                break
        if i==2:
            allzeros = True

        # Convert direction vector into unit vector
        if allzeros == False:
            norm=newDirec/np.sqrt(np.sum(newDirec**2))
        # BUT... if all direction vector elements are zero, direction vector is already a unit vector.
        else:
            norm = newDirec

        print("MC Thread: New course in (x, y, z): " + str(norm))
        #thr_arr = thr.split(" ")
        #thr_arr = [int(thr_arr[0]), int(thr_arr[1]), int(thr_arr[2])]
        #print("[" + str(thr_arr[0]) + "," + str(thr_arr[1]) + "," + str(thr_arr[2]) + "]")
        k=[0,0,1]
        n=np.cross(k,norm) #n is the vector to be expressed by servos
        #print ("Vector to be expressed by servos: ", n)
        
        x_pwm=400+n[0]*100 #x component of n as a pwm
        y_pwm=400+n[1]*140 #y component of n as a pwm
        #print ("x_pwm:", x_pwm)
        #print ("y_pwm:", y_pwm)
        
        self.pwm.set_pwm(0, 0, int(x_pwm))
        self.pwm.set_pwm(1, 0, int(y_pwm))
