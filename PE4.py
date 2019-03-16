import math

def has_3digit_factors(n):
	i = 100
	while i < math.floor(math.sqrt(n)):
		if n%i == 0:
			if len(str(i)) == 3 and len(str(int(n/i))) == 3:
				return True
		i += 1
	return False

n = 999999
it = 0
breakloops = False

while n > 100000 and not has_3digit_factors(n):
	it +=1
	if it%100 == 0:
		n -= 11
	elif it%10 == 0:
		n -= 110
	else:
		n -= 1100

print(n)