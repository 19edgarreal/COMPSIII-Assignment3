class Person:
    # Delete pass and add your code here
    def __init__(self, name, age, country):
    self.name = name
    self.age = age
    self.country = country
   
    def __str__(self):
    return f"{self.name} is {self.age} years old and is from {self.country}."

class Student(Person):
    # Delete pass and add your code here
    pass

class Staff(Person):
    # Delete pass and add your code here
    pass
