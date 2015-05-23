#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def mult_3or5():
    for num in xrange(1000):
        if not num % 3 or not num % 5:
            yield num

print sum(mult_3or5())
