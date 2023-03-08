class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class Emp(person):

    def __init__(self, name, id):
        self.name_ = name
        super().__init__(name,id)

        def print(self):
            print("Emp class called")


emp_info = Emp("NK", 12323)

print(emp_info.name,emp_info.name_)