def fib():
	x,y = 0,1
	while True:
		yield x
		x,y = y, x+y
	
def is_even(set):
	for n in set:
		if not n % 2:
			yield n
			
def under_mill(set):
	for n in set:
		if n > 4000000:
			break
		yield n

print sum(is_even(under_mill(fib())))