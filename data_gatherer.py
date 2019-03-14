import csv
import gps_gatherer
import 9dof_gatherer

class DataGatherer:

    def __init__(self, gpsGatherer, 9DofGatherer):
        self._gpsGatherer = gpsGatherer
        self._9DofGatherer = 9DofGatherer
    
    def gather(self):
        data = []
        data.append(self._gpsGatherer.gather())
        data.append(self.__9DofGatherer.gather())
        return data
    
    def writeToCSV(self, data):



if __name__ == "__main__":
    bob = DataGatherer(gpsGatherer, 9DofGatherer)
    data1 = bob.gather()
    bob.writeToCSV(data1)