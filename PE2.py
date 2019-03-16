fib1 = 1
fib2 = 2
fibsum = 0
sum = 2

while fibsum < 4000000:
	fibsum = fib1 + fib2
	if fibsum%2 == 0:
		sum += fibsum
	fib1 = fib2
	fib2 = fibsum
	
print(sum)