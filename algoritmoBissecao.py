import math
def samesign(a, b):
	return a * b > 0

def bisect(func, low, high, tolerance=10**-3): #tolerance 10^-3 (ERRO)

	for i in range(54):
	    midpoint = (low + high) / 2.0
	    if samesign(func(low), func(midpoint)):
		    low = midpoint
	    else:
		    high = midpoint
	    if tolerance is not None and abs(high - low) < tolerance:
		    break   
	return midpoint

def f(x):
	# x^3 - 10 = 0
	return -10 + x**3

# parametros >>> bissecao(f(x), a, b)
x = bisect(f, 0, 5)

#saída >>> Raíz e f(x)
print(x, f(x))