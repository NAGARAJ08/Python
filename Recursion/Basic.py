#print 1 to n or n to 1

def recursion(n):
    
    if n==0:
        return 
    
    
    print(n,end=" ")
    recursion(n-1)
    print(n,end = " ")
    
recursion(10)
    