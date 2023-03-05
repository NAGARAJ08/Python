# select the smallest element from unsorted list to the sorted list

def selection_sort(arr,n):
    
    for i in range(n):
        
        minidx = i
        
        for j in range(i+1,n):
            
            if arr[j]<arr[minidx]:
                minidx = j
        
        (arr[i],arr[minidx]) = (arr[minidx],arr[i])
        
    
n = int(input("Enter the number of ele:\t "))

arr = []

for i in range(0,n):
    v = int(input())
    arr.append(v)

selection_sort(arr,n)

print(arr)
