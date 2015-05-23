#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

largest = 0
for n in xrange(999, 100, -1):
	for m in xrange(n, 100, -1):
		p = n * m
		if p > largest:
			s = str(n * m)
			if s == s[::-1]:
				largest = n * m
print largest