from classes.servo import Servo
from adafruit_servokit import ServoKit

class LaserHead:
    def __init__(self):
        self.kit = ServoKit(channels=16)
        
        self.pan = Servo(self.kit.servo[0], minPulseWidth=600, maxPulseWidth=2645)
        self.tilt = Servo(self.kit.servo[1], minPulseWidth=480, maxPulseWidth=2675)

    def reset(self):
        self.pan.mid()
        self.tilt.mid()

    def test_servoRange(self):
        from time import sleep

        self.reset()
        sleep(0.5)

        self.pan.min()
        print(self.pan.getAngle())
        sleep(2)
        self.pan.max()
        print(self.pan.getAngle())
        sleep(2)
        self.pan.mid()
        print(self.pan.getAngle())
        sleep(2)

        self.tilt.min()
        print(self.tilt.getAngle())
        sleep(2)
        self.tilt.max()
        print(self.tilt.getAngle())
        sleep(2)
        self.tilt.mid()
        print(self.tilt.getAngle())
        sleep(2)

        self.reset()



