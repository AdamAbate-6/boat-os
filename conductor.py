import time
import sys
sys.path.insert(0, '/home/pi/boat-os/observing')
sys.path.insert(0, '/home/pi/boat-os/control')

import data_gatherer as dg
import gather_test as gt
import motor_controller as mc


#gather = gt.DataGathererTest(0.1)
#Create a data-gathering thread that runs with 0.1 s delays, not including motor-adjustment time
dataGatherer = dg.DataGatherer(0.1)
#Create a motor-controlling thread that runs with 0.1 s delays, not including data-gathering time
motorControl = mc.MotorController(0.1, 1000)

#gather.start()
dataGatherer.start()
motorControl.start()

#gather.join()
# dataGatherer.join() means that this script cannot do anything else until dataGatherer stops running
dataGatherer.join()
# motorControl.join() means that this script cannot do anything else until motorControl stops running
motorControl.join()