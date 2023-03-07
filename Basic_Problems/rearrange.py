def solve(arr):
    for i in range(0,n-1,2):
        arr[i],arr[i+1] = arr[i+1],arr[i] #swapping the elements
    return arr

n = 5
arr = [1,2,3,4,5]
print(solve(arr))