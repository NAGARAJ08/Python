def binary_search(arr,key):

    l = 0
    h = len(arr)-1

    while l<=h:

        m = l + (h-l)//2

        if arr[m]==key:
            return m
        elif arr[m] > key:
            h = m -1
        else:
            l = m +1
    return -1


a = []

n = int(input("enter the size of the array"))
print("Enter the array")

for i in range(0,n):
    v = int(input())
    a.append(v)

print("Enter the key to be find")
key = int(input())

print(binary_search(a,key))