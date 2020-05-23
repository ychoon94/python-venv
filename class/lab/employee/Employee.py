class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increment(self, amount):
        self.salary = self.salary + amount
        return self.salary

    def higherThan(self, other):
        if self.salary > other.salary:
            return True
        elif other.salary > self.salary:
            return False
        else:
            return NotImplemented
