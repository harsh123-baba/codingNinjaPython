class Vehicle:
    def __init__(self, color, maxspeed):
        self._color = color
        self.__maxspeed = maxspeed

    def getMaxSpeed(self):
        return self.__maxspeed
    def setMaxSpeed(self, maxspeed):
        self.__maxspeed = maxspeed
    
    def Print(self):
        print("Color : ", self._color)
        print("MaxSpeed : ", self.getMaxSpeed())




class Car(Vehicle):
    def __init__(self, color, maxspeed, gears):
        super().__init__(color, maxspeed)
        self.gears = gears

    def PrintCar(self):
        super().Print()
        print("Gears : ", self.gears)

c = Car("Blue", 120, 5)
c.PrintCar()
print(Car.mro())