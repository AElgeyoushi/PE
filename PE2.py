even_fib = set()
fib1 = 1
fib2 = 2
even_fib.add(fib2)
fibsum = 0

while fibsum < 4000000:
	fibsum = fib1 + fib2
	if fibsum%2 == 0:
		even_fib.add(fibsum)
	fib1 = fib2
	fib2 = fibsum
	
sum = 0
while len(even_fib) != 0:
	n = even_fib.pop()
	sum += n
	
print(sum)