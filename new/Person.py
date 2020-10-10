class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return self.__name + " is " + str(self.__age)

    def birthday(self):
        print("HBD")
        self.__age += 1
        print("you are now", self.__age)