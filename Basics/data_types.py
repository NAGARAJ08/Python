def numeric():

    a = 10
    b = 10.0
    c = 10+4j

    print(a,type(a))
    print(b,type(b))
    print(c,type(c))

def string_type():

    str  = "Hello! There "
    
    print(str,type(str))
    print(str[:6])
    print(str[7:])

    print(str[-1])
    print(str*2)
    print(len(str))


def list_type():
    lst = ["A" , 1 , "B", 2, "C", 3]

    print(lst)
    print(type(lst))

    print(len(lst))

    lst.append("D")
    lst.append(4)

    print(lst)
    print(lst[0:3])

    print(lst[3:])

    print(lst[-1])

    print(lst[-2])
    


def tuple_type():
    # Tuples are immutable

    tup = ("L",11,"M",12,"N",13)
    print(tup)
    print(type(tup))

    # we cannot add,delete to tuples


def _range_():

    # range(start,stop,increment)--> Syntax
    for i in range(1,6): 
        # 6 is excluded here 
        print(i)
    
    print()
    
    for _ in range(1,5,2):
        # increment by 2 each time
        print(_)



def dict_type():
    
    dict = {'Id':12,'Name':'XYZ','Location':'Bangalore'}

    print(dict)

    # print(type(dict))

    print(dict.keys())
    print(dict.values())

    thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
    }

    print(thisdict)
    print(thisdict["brand"])
    print(thisdict["colors"])

    
def bool_type():

    a,b,c = 3,4,3

    print(a==b)

    # print(bool(a))

    print(a==c)

    print(a!=b)



# numeric()
# string_type()

# list_type()
# tuple_type()

# _range_()

dict_type()
# bool_type()
