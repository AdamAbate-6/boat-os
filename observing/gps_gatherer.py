import gps

class GpsGatherer:

    def __init__(self):
        # Listen on port 2947 (gpsd) of localhost
        self.session = gps.gps("localhost", "2947")
        self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
        #Input GPS data, output integer in format hoursminutessecondsmilliseconds
        self.rawToAct = lambda x : int(x[11:13] + x[14:16] + x[17:19] + x[20:23])
    
    def gather(self):
        reports = []

        # Number of empty reports -- specific to GPS module
        numInitReports = 3
        # Number of data-filled reports to gather
        numReps = 1

        for i in range(0, numReps + numInitReports):
            try:
                report = self.session.next()
                # Wait for a 'TPV' report and display the current time
                # To see all report data, uncomment the line below
                #print(report)
                if report['class'] == 'TPV':
                    if (hasattr(report, 'time') and hasattr(report, 'lat') and hasattr(report, 'lon')):
                        #print(report.time)
                        #print("Lat/Lon: " + str(report.lat) + ", " + str(report.lon))
                        report = [report.time, report.lat, report.lon]
                        reports.append(report)
            except KeyError:
                pass
            except KeyboardInterrupt:
                quit()
            except StopIteration:
                self.session = None
                print("GPSD has terminated")
        
        return reports