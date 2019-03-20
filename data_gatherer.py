import csv
import gps_gatherer
import 9dof_gatherer

class DataGatherer:

    def __init__(self, gpsGatherer, 9DofGatherer):
        self._gpsGatherer = gpsGatherer
        self._9DofGatherer = 9DofGatherer
    
    def gather(self):
        data = []
        #Append gps lat/lon lists
        data.append(self._gpsGatherer.gather())
        #Append 9dof matrix of mag, accel, and gyr lists
        data.append(self._9DofGatherer.gather())
        return data
    
    def writeToCSV(self, data):
        with open('data.csv', 'w') as csvfile:
            #Initialize csvfile writer
            fieldnames = ['gps_lat', 'gps_lon', '9dof_m_x', '9dof_m_y', '9dof_m_z']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            #Format csv and write data
            writer.writeheader()
            writer.writerow({'gps_lat': data[0][0], 'gps_lon': data[0][1], '9dof_m_x': data[1][0][0], '9dof_m_y': data[1][0][1], '9dof_m_z': data[1][0][2]})

if __name__ == "__main__":
    dgat = DataGatherer(gpsGatherer, 9DofGatherer)
    data = dgat.gather()
    dgat.writeToCSV(data)