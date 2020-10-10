def f(a, b):
    return a + b

from Person import Person
from Employee import Employee


p1 = Person("ali", 45)


class Toy:
    def move(self):
        print("Toy")


class Car:
    def move(self):
        print("Car")


class ToyCar(Toy, Car):
    pass

