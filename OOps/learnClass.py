class Car:

    # __init__ method acts as equivalent to constructor
    def __init__(self,model,year):
        # self reference to the current instance of the class
        #self is also used to access the var belongs to the class
        self.model = model
        self.year  = year

    def display(self):
        print(self.model,self.year)



'''
Class - Design/blueprint

Object - Instance of class


object has two things :

attributes and behaviour

attributes - eg: age,id,name,salary,companies etc

behaviour - eg: barking,talking,dancing
'''
car1 = Car("TATA Nexon",2020)

# this calls the display method of the class Car
car1.display()
