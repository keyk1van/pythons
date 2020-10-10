class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __str__(self):
        return self.name + " is " + str(self.age)

