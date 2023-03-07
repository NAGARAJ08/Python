def missing_ele(array,n):
    sum =0
    i=0
    while i<n-1:
        sum +=array[i]
        i+=1
    res=0
    res = n*(n+1)/2
    res = int(res-sum)

    return res

n = int(input("Enter the size of array "))

a1 = []


print("Enter the elemnets of array")
for i in range(n-1):
    v = int(input())
    a1.append(v)

print(missing_ele(a1,n))