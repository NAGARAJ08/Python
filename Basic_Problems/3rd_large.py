def third_largest(arr,n):
    
    if n<3:
        return "-1"
    
    arr.sort()
    return arr[2]
    
n = int(input("Enter the number of ele:\t "))

arr = []

for i in range(0,n):
    v = int(input())
    arr.append(v)

print(third_largest(arr,n))