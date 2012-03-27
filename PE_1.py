def mult_3or5():
    for num in xrange(1000):
        if not num % 3 or not num % 5:
            yield num

print sum(mult_3or5())
