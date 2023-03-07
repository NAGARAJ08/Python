
def search(arr,X,n):

    i=0
    while(i<n):
        if arr[i]==X:
            return i
        i+=1
    return -1


n = int(input("Enter the size of array "))

a1 = []


print("Enter the elemnets of array")
for i in range(n):
    v = int(input())
    a1.append(v)

x = int(input("Enter the ele to search: "))

res = search(a1,x,n)

print(res)