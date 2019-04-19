import time
import board
import busio
import adafruit_fxos8700

class NineDOFGatherer:

    def __init__(self):
        # Initialize I2C bus and device.
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_fxos8700.FXOS8700(self.i2c)

    def gather(self):
        data = []
        data.append(self.sensor.magnetometer)
        data.append(self.sensor.accelerometer)
        return data

