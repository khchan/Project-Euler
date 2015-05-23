#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

s1 = xrange(1, 101)
s1_sum = sum(s1)

s2 = 0
for n in s1:
	s2 = s2 + n * n
	
print s1_sum * s1_sum - s2