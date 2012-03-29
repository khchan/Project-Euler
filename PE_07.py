#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

def isprime(n):
	i = 2
	while i * i <= n:
		if n % i == 0:
			return 0
		i = i + 1
	return 1
	
cur = 2
i = 0
prime = 0

while i != 10001:
	if isprime(cur) == 1:
		i = i + 1
		prime = cur
	cur = cur + 1

print prime