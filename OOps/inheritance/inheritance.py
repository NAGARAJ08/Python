# Multi Level
'''
Vehicle
   ^
   |
  Car
   ^
   |
RaceCar

'''


class Vehicle():

    def type(self):
        print("\nits an automobile (motor driven)")



class Car(Vehicle):

    def price(self):
        print("Price of the car ")
    
    def colour(self):
        print("Colour of the car")



class RaceCar(Car):

    def navigator(self):
        print("Race Car has Navigator")
    
    def Timer(self):
        print("Car has timer\n")




# c1 = Car()
# c1.price()
# c1.colour()

c2 = RaceCar()
c2.type()
c2.navigator()
c2.colour()
c2.price()
c2.Timer()
