"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

def tri_num(n):  
    return n*(n+1)/2 

def prime_factors(n):
    for x in xrange(2,n):
        if n%x == 0:
            return (x,) + prime_factors(n/x)
    return (n,1)
	
def divisors(m):
	div = 1
	alist = prime_factors(m)
	set_list = [(alist.count(a)) for a in set(alist)]
	for x in set_list:
		div = div * (x+1)
	return div

i = 1
while True:
	if divisors(tri_num(i))/2 >= 500:
		print tri_num(i)
		break
	i += 1