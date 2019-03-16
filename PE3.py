import math

n = 600851475143 
i = 1
while i < math.sqrt(n):
	if n%i == 0:
		n = n/i
	i += 1
print(n)