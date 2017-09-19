def fib(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return fib(n-1)+fib(n-2)

print ("fib de 1 es %d"% fib(1))
print ("fib de 2 es %d"% fib(2))
print ("fib de 5 es %d"% fib(5))
