def immediate_smaller(a,n):
    
    for i in range(n):
        
        if i+1 == n:
            a[i]=-1
        else:
            if a[i+1]<a[i]:
                a[i]=a[i+1]
            else:
                a[i]=-1
    return a
    

n = int(input("Enter the number of ele:\t "))

arr = []

for i in range(0,n):
    v = int(input())
    arr.append(v)

print(immediate_smaller(arr,n))