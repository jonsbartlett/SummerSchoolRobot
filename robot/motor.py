class Motor:
    def __init__(self, transmitter, number, speed = 0):
        self.t = transmitter
        self.number = number
        self.speed = speed       

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self,speed):
        if speed > 100:
            self.__speed = 100
            print("Motor",self.number,"speed out of allowed range.  Set to 100.")
        elif speed <-100:
            self.__speed = -100
            print("Motor",self.number,"speed out of allowed range.  Set to -100.")
        else:
            self.__speed = speed
        self.t.transmit("motor",self.number,self.speed)
