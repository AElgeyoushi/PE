import math

def trianglar(n):
	return int(n*(n+1)/2)
	
def num_of_factors(n):
	i = 1
	factors = 0
	
	while i < math.sqrt(n):
		if n%i == 0:
			factors += 2
		i += 1
	
	return factors

i = 1
while num_of_factors(trianglar(i)) < 500:
	i += 1
print(trianglar(i))	