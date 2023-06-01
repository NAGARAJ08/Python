def fib(num):
    
    if num==1 or num==0:
        return 1
    
    return fib(num-1)+fib(num-2)

ans = fib(5)
print(ans)