def fib(n,k=1):
    if(n <= 2): return 1
    else: return ((fib(n-2,k)*k)+fib(n-1,k))

print(fib(36,5))
