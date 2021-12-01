from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, wheels):
        self.wheels = wheels
        print("Vehicle Called")

    @abstractmethod
    def getWheels(self):
        return self.wheels
    @abstractmethod
    def start(self):
        print("Hii")

class Car(Vehicle):

    def start(self):
        super().start()

    def getWheels(self):
        return super().getWheels()

class Bus(Vehicle):
    def start(self):
        super().start()


    def getWheels(self):
        return super().getWheels()

c = Car(4)
b = Bus(8)

c.start()

print(c.getWheels())


