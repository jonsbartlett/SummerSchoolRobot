from servo import *
from transmit import *
from motor import *
from vision import *

numOfMotors = 4
numOfServos = 8

class Robot:
    'A robot object which contains lists of the available parts'
    def __init__(self):
        self.t = Transmitter()
        self.servo = []
        self.motor = []
        self.cam = Vision()
        for i in range(numOfServos):
            self.servo.append(Servo(self.t,i))
        for i in range(numOfMotors):
            self.motor.append(Motor(self.t ,i))

    def see(self, (x,y) = (800,600), preview = False, preview_time = 1):
        return self.cam.vision_see((x,y), preview, preview_time)
    

    
