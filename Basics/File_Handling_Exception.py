try:
    file1 = open("Ra.txt",'r')
    read_data = file1.read()
    print(read_data)
except FileNotFoundError as F:
    print(F)