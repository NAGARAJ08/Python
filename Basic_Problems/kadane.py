def maximum_subarray(arr,n):
    
    max_sum = arr[0]
    cursum = 0
    
    for i in range(n):
        cursum = cursum+arr[i]
        if cursum > max_sum:
            max_sum = cursum
        if cursum < 0 :
            cursum = 0
    return max_sum
    


n = int(input("Enter the number of ele:\t "))

arr = []

for i in range(0,n):
    v = int(input())
    arr.append(v)


print(maximum_subarray(arr,n))