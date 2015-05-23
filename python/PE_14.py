
def hailstone(n):
	count = 0
	while n > 1:
		if n % 2 == 0: n = n/2
		else: n = 3*n + 1
		count += 1
	return count

max = 0
ind = 0
cur = 0

for x in range(1, 100000):
	cur = hailstone(x)
	if cur > max:
		max = cur
		ind = x

print max, ind