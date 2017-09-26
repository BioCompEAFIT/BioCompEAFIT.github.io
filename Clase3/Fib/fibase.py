def fib(n,k=1):
    if(n <= 2): return 1
    else: return (fib(n-1)+fib(n-2))

print(fib(34,5))
