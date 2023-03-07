def check(arr1,arr2):

    arr1.sort()
    arr2.sort()

    if arr2==arr1:
        return True
    else:
        return False


n = int(input("Enter the size of both arrays "))

a1 = []
a2 = []

print("Enter the elemnets of first array")
for i in range(n):

    v = int(input())
    a1.append(v)

print("Enter the elemnets of second array")
for i in range(n):
    v = int(input())
    a2.append(v)


print("Are both arrays same: ",check(a1,a2))
