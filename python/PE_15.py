#Starting in the left of a 2x2 grid, there are 6 routes.
#How many routes are there in a 20x20 grid?

from math import factorial

def pascal(n):
	return factorial(2*n)/(factorial(n)*factorial(n))
	
print pascal(20)