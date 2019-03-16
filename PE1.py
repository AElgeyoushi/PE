mul_of_5 = set()
mul_of_3 = set()
complete = set()
sum = 0

i = 5
while i < 1000:
	mul_of_5.add(i)
	i += 5
	
i = 3
while i < 1000:
	mul_of_3.add(i)
	i += 3
	
complete = mul_of_5.union(mul_of_3)

while len(complete) != 0:
	n = complete.pop()
	sum += n

print(sum)