class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id


class Dev(Employee):

    def __init__(self, name, id, language):
        """
        Instead of writing the self.name =name ,self.id = id

        we could use the parent class init method to do so

        hence we called the super method for this

        CODE REUSABILITY

        """
        super().__init__(name, id)
        self.language = language


DEV1 = Dev("NK", 1231, "Python")
emp1 = Employee("SKD", 3221)

print(DEV1.name, DEV1.id, DEV1.language)
print(emp1.name, emp1.id)
