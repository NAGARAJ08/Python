# Try Catch
try:
    # val = 10/0
    num = int(input("Enter the num"))
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError as ER:
    print(ER)
