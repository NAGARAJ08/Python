'''
This is a Simple Python Calculator
'''
def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def Mul(a,b):
    print(a*b)

def div(a,b):
    try:
        print(a/b)
    except ZeroDivisionError as e:
        print("This is Divison Error",e)


def Calculator():

    while True:
        # print("Enter the Numbers: ")

        choice = input("1:Addition 2:Subtraction 3:Multiplication 4:Division\n")
        if choice in ("1","2","3","4"):
            try:
                a = float(input("Enter the a: "))
                b = float(input("Enter the b: "))
            except ValueError as v:
                print("This is value error ",v)
                continue
        else:
            print("Enter the Valid Input")
            Calculator()


        if choice=="1":
            add(a,b)
        elif choice=="2":
            sub(a,b)
        elif choice=="3":
            Mul(a,b)
        elif choice=="4":
            div(a,b)

        request = input("Do you want to perform another Calculation: (Yes || No )\n")
        if request == "no":
            break;    



Calculator()