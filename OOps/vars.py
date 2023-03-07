
'''
Two types of var :

instance variables and Classic(static) Variable

'''
class Car:

    # Class var
    wheels = 4
    def __init__(self):
        # There are instance variables
        self.company = "BMW"
        self.milage = 22

car1 = Car()
car2 = Car()

car2.milage = 18

# to Modifying the static var we use class name

Car.wheels = 6    


print(car1.company,car1.milage,car1.wheels)
print(car2.company,car2.milage,car2.wheels)