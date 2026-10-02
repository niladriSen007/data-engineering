

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is starting...")
        
class Bike(Vehicle):
    def start(self):
        print("Bike is starting...")
        
my_car = Car()
my_car.start()
my_bike = Bike()
my_bike.start()