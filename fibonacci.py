from math import sqrt 
def Fibonacci(n):

	if n == 0: 
		return 0
    
	elif n == 1: 
		return 1
    
	else: 
		return Fibonacci (n - 2) + Fibonacci (n - 1)

def Fib(n):

    k = (1 / (sqrt(5)))*(((1 + (sqrt(5))) / 2))**n
    return round(k)

def Fibon(n):
	a = 0
	b = 1 
	d = 1
	while d != n:
		c = a + b
		a = b 
		b = c
		d = d + 1 
	return c
	

print (Fibonacci(15))
print (Fib(100))
print (Fibon(100))

