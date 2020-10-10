from Person import Person


class Employee(Person):
    def __init__(self, name, age, idd):
        super().__init__(name, age)
        self.idd = idd

    def calculate_pay(self, hours):
        pay_of_rate = 7.5
        if self.age > 21:
            pay_of_rate += 2.5
        return hours * pay_of_rate
