class student:
    
    # Outer Class
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name,self.rollno)

        

    # Inner class 
    class Laptop:

        def __init__(self):
            self.brand = 'DELL'
            self.cpu = 'i7'
            self.ram = 16

s1 = student('Navin',212)
s2 = student('Raj',321)

s1.show()
s2.show()

lap1 = s1.lap


print(lap1.brand)
print(s1.lap.cpu)


