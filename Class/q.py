class Person:
    def __init__(self, first_name, last_name, age):
        self.firs_name = first_name
        self.last_name = last_name
        self.age = age
    def __str__(self):
        return self.firs_name + ' ' + self.last_name


jack = Person(input(), input(), input())
print(jack)