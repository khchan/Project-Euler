def mult_3_or_5():
    for n in xrange(1000):
        if not n % 3 or not n % 5:
            yield n

print sum(mult_3_or_5())
