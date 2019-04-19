import threading
import time
import random
import csv

import direc_controller as dc
import speed_controller as sc

class MotorController(threading.Thread):

    def __init__(self, delay, runSpeed):
        threading.Thread.__init__(self)
        self.delay = delay

        self.direcController = dc.DirectionController()
        self.speedController = sc.SpeedController(runSpeed)

        self.speedController.armESC()
        
    
    def run(self):
        # Randomly assign direction vectors
        #direcVec = [[0,0,1], [0,1,1], [1,1,1], [1,1,0], [1,0,0], [0,0,0], [0,1,0]]
        #direcVec = [[0,0,0]]

        while 1:

            # Make robot north-seeking
            northVec = []
            newDirec = []
            with open('/home/pi/boat-os/data.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    #print(row)
                    if (len(row) == 6):
                        if(row["9dof_m_x"] is not None and row["9dof_m_y"] is not None and row["9dof_m_z"] is not None):
                            northVec = [float(row["9dof_m_x"]), float(row["9dof_m_y"]), float(row["9dof_m_z"])]
                            # New thrust vector should be opposite north
                            newDirec = [-northVec[0], -northVec[1], -northVec[2]]
            
            #print("North vector: " + str(northVec))

            print("MC Thread: Running VSD")
            self.speedController.runESC()
            print("MC Thread: Speed control complete")

            # Random vector selection
            #newDirec = direcVec[random.randint(0, len(direcVec)-1)]

            if (len(newDirec) == 3):
                print("MC Thread: Adjusting servo direction")
                self.direcController.adjustServos(newDirec)
                print("MC Thread: Direction control complete")
            else:
                print("MC Thread: Not adjusting servos -- no input direction!")


            time.sleep(self.delay)
    