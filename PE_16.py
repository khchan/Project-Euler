#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
#What is the sum of the digits of the number 2^1000

num = str(pow(2, 1000))
tot = 0
for i in xrange(0, len(num)):
	tot = tot + int(num[i])

print tot
