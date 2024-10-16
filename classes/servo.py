from time import sleep

class Servo:
    def __init__(self, servo, minPulseWidth, maxPulseWidth):
        # takes in a servo from adafruit_servokit's ServoKit.servo[] 
        self.servo = servo
        self.min_pulse_width = minPulseWidth
        self.max_pulse_width = maxPulseWidth

        self.setPulseWidthRange(self.min_pulse_width, self.max_pulse_width)

    def setPulseWidthRange(self, minPulseWidth, maxPulseWidth):
        self.min_pulse_width = minPulseWidth
        self.max_pulse_width = maxPulseWidth
        
        self.servo.set_pulse_width_range(self.min_pulse_width, self.max_pulse_width)
    
    def getPulseWidthRange(self):
        return self.min_pulse_width, self.max_pulse_width

    def min(self):
        self.servo.angle = 0

    def mid(self):
        self.servo.angle = 90

    def max(self):
        self.servo.angle = 180

    def getAngle(self):
        return self.servo.angle
    
    def setAngle(self, angle):
        self.servo.angle = angle