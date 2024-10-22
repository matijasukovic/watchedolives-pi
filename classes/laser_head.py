from classes.servo import Servo
from adafruit_servokit import ServoKit
import math

class LaserHead:
    def __init__(self):
        self.kit = ServoKit(channels=16)
        
        self.pan = Servo(self.kit.servo[0], minPulseWidth=600, maxPulseWidth=2645)
        self.tilt = Servo(self.kit.servo[1], minPulseWidth=480, maxPulseWidth=2675)

    def reset(self):
        self.pan.mid()
        self.tilt.mid()

    def setPanAngle(self, angle):
        if angle < 0:
            self.pan.setAngle(0)
        elif angle > 180:
            self.pan.setAngle(180)
        else:
            self.pan.setAngle(angle)

    def setTiltAngle(self, angle):
        min, max = self.getTiltAngleLimits()

        if angle < min:
            self.tilt.setAngle(min)
        elif angle > max:
            self.tilt.setAngle(max)
        else:
            self.tilt.setAngle(angle)


    def getTiltAngleLimits(self):
        p = abs(math.cos(2 * math.radians(self.pan.getAngle())))

        minAngle_lowerLimit = 43
        minAngle_upperLimit = 54

        minAngle = minAngle_lowerLimit + (minAngle_upperLimit - minAngle_lowerLimit) * p

        maxAngle_lowerLimit = 119
        maxAngle_upperLimit = 125

        maxAngle = maxAngle_lowerLimit + (maxAngle_upperLimit - maxAngle_lowerLimit) * (1 - p)

        if (0 <= self.pan.getAngle() <= 38 and self.tilt.getAngle() > 90) or (139 <= self.pan.getAngle() <= 180 and self.tilt.getAngle() < 90):
            # Pointing to the right side of the image (farther from the laser head), slightly increase limits
            minAngle = minAngle - 3
            maxAngle = maxAngle + 7 
        elif (0 <= self.pan.getAngle() <= 38 and self.tilt.getAngle() < 90) or (139 <= self.pan.getAngle() <= 180 and self.tilt.getAngle() > 90):
            # Pointing to the left side of the image (closer to laser head), decrease limits slightly
            minAngle = minAngle + 6
            maxAngle = maxAngle - 1

        return minAngle, maxAngle


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



