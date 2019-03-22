import time
import sys
sys.path.insert(0, '/home/pi/boat-os/observing')
sys.path.insert(0, '/home/pi/boat-os/control')

import data_gatherer as dg
import motor_controller as mc


#Create a data-gathering thread that runs with 0.1 s delays, not including motor-adjustment time
dataGatherer = dg.DataGatherer(0.1)
#Create a motor-controlling thread that runs with 0.1 s delays, not including data-gathering time
motorControl = mc.MotorController(0.1)

dataGatherer.start()
motorControl.start()

# dataGatherer.join() means that this script cannot do anything else until dataGatherer stops running
dataGatherer.join()
# motorControl.join() means that this script cannot do anything else until motorControl stops running
motorControl.join()