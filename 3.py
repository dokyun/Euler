x = []
target = 600851475143
count = 0
for i in range (3,100000):
	for j in range (2,i):
		if i%j == 0:
			count += 1
			break
	if count == 0:
		if target%i == 0:
			x.append(i)
			print i,
	count = 0
