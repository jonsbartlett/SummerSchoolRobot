#Making a class to represent a servo

class Servo:
    'This class represents a servo motor attached to the robot'
    
    def __init__(self, transmitter,number, position = 0):
        self.t = transmitter
        self.number = number
        self.position = position
                
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self,position):
        if (position < 100) and (position > -100):
            self.__position = position
            self.t.transmit("Servo",self.number,position)
        else:
            print("Servo", self.number, "value out of allowed range")

    
            
    
