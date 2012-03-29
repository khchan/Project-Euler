#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from fractions import gcd

def lcm(a, b):
	return a * b / gcd(a,b)

val = 1	
for n in range(1, 21):
	val = lcm(val, n)
	
print val