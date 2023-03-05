# places an unsorted element at its suitalbe place in each iteration

def insertion_sort(arr):
    
    for i in range(1,len(arr)):
        
        key = arr[i]
        j = i-1
        
        while j>=0 and key < arr[j]:
            
            arr[j+1] = arr[j]
            j = j-1
            
        arr[j+1] = key
        
        
    
n = int(input("Enter the number of ele:\t "))

arr = []

for i in range(0,n):
    v = int(input())
    arr.append(v)
    
insertion_sort(arr)

print(arr)
    