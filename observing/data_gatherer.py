import csv
import time
import threading

import gps_gatherer as gg
import nine_dof_gatherer as dg

class DataGatherer(threading.Thread):

    def __init__(self, delay):
        self._gpsGatherer = gg.GpsGatherer()
        self._9DofGatherer = dg.NineDOFGatherer()
        self.delay = delay
        threading.Thread.__init__(self)
    
    def gather(self):
        data = []
        #Append gps lat/lon lists
        data.append(self._gpsGatherer.gather())
        #Append 9dof matrix of mag, accel, and gyr lists
        data.append(self._9DofGatherer.gather())
        return data
    
    def writeToCSV(self, data):
        with open('/home/pi/boat-os/data.csv', 'w') as csvfile:
            #Initialize csvfile writer
            fieldnames = ['gps_time', 'gps_lat', 'gps_lon', '9dof_m_x', '9dof_m_y', '9dof_m_z']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            #Format csv
            writer.writeheader()

            # Write none to field if we don't have data for it.
            if(data[0] == []):
                writer.writerow({'gps_time': None, 'gps_lat': None, 'gps_lon': None, '9dof_m_x': data[1][0][0], '9dof_m_y': data[1][0][1], '9dof_m_z': data[1][0][2]})
            elif (data[1] == [[],[]]):
                writer.writerow({'gps_time': data[0][0], 'gps_lat': data[0][1], 'gps_lon': data[0][2], '9dof_m_x': None, '9dof_m_y': None, '9dof_m_z': None})
            elif (data[0] == [] and data[1] == [[],[]]):
                writer.writerow({'gps_time': None, 'gps_lat': None, 'gps_lon': None, '9dof_m_x': None, '9dof_m_y': None, '9dof_m_z': None})
                print("No data written to CSV!")
            else:
                writer.writerow({'gps_time': data[0][0], 'gps_lat': data[0][1], 'gps_lon': data[0][2], '9dof_m_x': data[1][0][0], '9dof_m_y': data[1][0][1], '9dof_m_z': data[1][0][2]})

    def run(self):
        while 1:
            print("DG Thread: Gathering data")
            data = self.gather()
            print("DG Thread: Writing the following data: " + str(data))
            self.writeToCSV(data)
            print("DG Thread: Data written to CSV")
            time.sleep(self.delay)
