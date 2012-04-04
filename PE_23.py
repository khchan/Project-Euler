'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that 
cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

from math import sqrt

def sum_factors(n):  
	sum = 0
	lim = sqrt(n)
	for i in range(2, int(lim)+1):
		if n % i == 0: 
			sum += i + n / i		
	if lim == int(lim):
		sum -= lim
	return sum
 
def check_set(set, i):
    for n in set:
        if i-n in set:
            return True
    return False
 
total = 0
abset = set()
for i in range(1, 28123):
	if sum_factors(i) > i:
		abset.add(i)
	if not check_set(abset, i):
		total += i		
print total