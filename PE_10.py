#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

from math import sqrt

list = [True] * 2000000

def tag(list, n):
	for i in xrange(n+n, len(list), n):
		list[i] = False

for i in range(2, int(sqrt(len(list))) + 1):
	if list[i]:	tag(list, i)

psum = 0
for i in range(2, len(list)):
	if list[i]:	psum += i
print psum