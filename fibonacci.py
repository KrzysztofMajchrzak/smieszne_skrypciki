def Fibonacci(n):

    if n == 0: return 0
    
    elif n == 1: return 1
    
    else: return Fibonacci (n - 2) + Fibonacci (n - 1)

def Fib(n):

    n = (1 / (5**(1/2)))*(((1 + (5**(1/2))) / 2))**n - (1 / (5**(1/2)))*(((1 - (5**(1/2))) / 2))**n
    return round(n)


print (Fibonacci(5))
print (Fib(5))

