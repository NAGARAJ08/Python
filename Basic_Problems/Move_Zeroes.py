def move_zeroes(arr):
    # arr = [5, 6, 0, 4, 6, 0, 9, 0, 8] 

    # list comprehension
    nonZeros =  [z for z in arr if z!=0]

    zeros = [x for x in arr if x==0]

    # print(nonZeros)

    Final_arr = nonZeros+zeros
    print(Final_arr)

a = []

n = int(input("enter the size of the array: "))
print("Enter the array")

for i in range(0,n):
    v = int(input())
    a.append(v)

move_zeroes(a)