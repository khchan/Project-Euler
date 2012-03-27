def palindrome():
	largest = 0
	for n in xrange(999, 100, -1):
		for m in xrange(n, 100, -1):
			p = n * m
			if p > largest:
				s = str(n * m)
				if s == s[::-1]:
					largest = n * m
	print largest

palindrome()