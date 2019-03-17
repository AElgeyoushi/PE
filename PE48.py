def find_last_digits(x, y, n):
	for i in range(1, y):
		x = (x * y) % n
	return x

last_ten = 0 
for i in range(1,1000):
	last_ten += find_last_digits(i,i,10000000000)
print(last_ten%10000000000)