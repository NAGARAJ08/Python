class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class Departments:

    def __init__(self):
        # print("This is Departments")
        pass


e1 = Employee("Raj", 21)
d1 = Departments()

# check whether the object e1 belongs to the class Employee class
# if belongs it returns true else false

print(isinstance(e1, Employee))  # this prints True

print(isinstance(d1, Employee))  # this prints False
