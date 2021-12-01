from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self):
        print("Class Called")

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def __init__(self):
        print("Car called")
    
    def start(self):
        pass
    def stop(self):
        pass
    def drive(self):
        pass

c = Car();
#we cant call the Vehicle class means we cant create the object of car class 
# it is abstract classs



