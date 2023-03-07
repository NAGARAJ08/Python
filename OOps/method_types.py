'''
-> Instance Methods
-> Class Methods
-> Static Methods

'''

class Student:

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    

s1 = Student(92,93,91)
s2 = Student(95,95,95)

print(s1.avg())
print(s2.avg())


