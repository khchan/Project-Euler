#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

val = 600851475143
n = 2

while n * n < val:
	while val % n == 0:
		val = val / n
	n = n + 1
print n