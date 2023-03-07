class student:

    def __init__(self,name,id,marks):
        self.name = name
        self.id = id
        self.marks = marks


s1 = student("ABC",1543,90)

# getattr(object, attribute, default)
val = getattr(s1,'name')
print(val)

# setattr(object, attribute, value)
setattr(s1,'marks',95)
print(getattr(s1,'marks'))


# the hasattr returns true if the student contains the id
print(hasattr(s1,'id'))


# deleting attribute
delattr(s1,'marks')

# print(getattr(s1,'marks'))  #this will pop the attribute error