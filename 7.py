x = []
count = 0
num = 9592#1
for i in range (100000,110000):
	for j in range (2,i):
		if i%j == 0:
			count += 1
			break
	if count == 0:
		num +=1
		if num == 10001:
			print i
			break
		x.append(i)
		print num,
	count = 0
