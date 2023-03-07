
# Multiple Inheritance
class Vehicle():

    def type(self):
        print("\nits an automobile (motor driven)")



class Car():

    def price(self):
        print("Price of the car ")
    
    def colour(self):
        print("Colour of the car")



class RaceCar(Vehicle,Car):

    def navigator(self):
        print("Race Car has Navigator")
    
    def Timer(self):
        print("Car has timer\n")



c1 = Car()
c2 = Vehicle()

c3 = RaceCar()
c3.type()
