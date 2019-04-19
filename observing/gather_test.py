# Simple demo of the FXOS8700 accelerometer and magnetometer.
# Will print the acceleration and magnetometer values every second.
import time
import board
import busio
import adafruit_fxos8700
import csv
import threading

class DataGathererTest(threading.Thread):

    def __init__(self, delay):
        # Initialize I2C bus and device.
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_fxos8700.FXOS8700(self.i2c)
    	
        self.delay = delay
        threading.Thread.__init__(self)

    def run(self):
        with open('/home/pi/boat-os/observing/mag_data_test.csv', 'w') as csvfile:
            csvWriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            fieldnames = ['9dof_m_x', '9dof_m_y', '9dof_m_z']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            while 1:
                mag_x, mag_y, mag_z = self.sensor.magnetometer
                csvWriter.writerow([mag_x, mag_y, mag_z])
                time.sleep(self.delay)