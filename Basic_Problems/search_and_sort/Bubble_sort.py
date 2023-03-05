def bubble_sort(arr,n):
    
    for i in range(n):
        
        swapped = False
        for j in range(n-i-1):
            
            if arr[j]>arr[j+1]:
                
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
                swapped = True
        
        if not swapped:
            break
            
    

    
n = int(input("Enter the number of ele:\t "))

arr = []

for i in range(0,n):
    v = int(input())
    arr.append(v)
    
bubble_sort(arr,n)

print(arr)
    

