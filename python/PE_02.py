#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

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