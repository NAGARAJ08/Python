
def min_max(a):

    mx = max(a)
    mn = min(a)

    return mx,mn

n = int(input("Enter the size of array "))

a1 = []


print("Enter the elemnets of array")
for i in range(n):
    v = int(input())
    a1.append(v)

print(min_max(a1))