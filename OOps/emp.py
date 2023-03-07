class employee:

    def __init__(self,name,id,designation,expertise):

        self.name = name
        self.id = id
        self.designation = designation
        self.expertise = expertise

    
emp1 = employee("ABC",24,"Product Manager","AIML")
emp2 = employee("RBC",25,"SDE","Python")


# emp1 and emp2 are the two objects instanciated the class employee
 

print(emp1.name,emp1.id,emp1.designation,emp1.expertise)
print(emp2.name,emp2.id,emp2.designation,emp2.expertise)



print(emp1.__dict__) #this prints all the info in dictionary format
print(emp2.__dict__)



# deleting the property of the object
del emp2.name
print(emp2.__dict__)

# deleting the object itself
del emp2
# print(emp2.__dict__) #this throws error