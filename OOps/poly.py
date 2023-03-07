# a = 5
# b = 4

# print(a+b)

# print(int.__add__(a,b))

class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self,other):

        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        st3 = student(m1+m2)

        return st3

s1 = student(45,49)
s2 = student(41,48)

s3 = s1 + s2  

print(s3.m1)
print(s3.m2)
