def linear_search(arr,n,x):
    
    for i in range(n):
        
        if arr[i]==x:
            return i
    return -1
    
    
    
n = int(input("Enter the number of ele:\t "))

arr = []

for i in range(0,n):
    v = int(input())
    arr.append(v)
    
X = int(input("Enter the element to search: "))


    
ans = linear_search(arr,n,X)

if ans == -1:
    print("Element Not found")
else:
    print("Element Found at index : ",ans)