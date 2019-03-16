import math

def isPrime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True
	
n = 2000000
sum = 0

i = 1
while i < n:
	if isPrime(i):
		sum += i
	i += 1
print(sum)

