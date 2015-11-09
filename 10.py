x = [2]
count = 0
i = 2
#num = 1
total = 2
while i < 2000000:#for i in range (3,100000):
	i += 1
	for j in x:
		if i%j == 0:
			count += 1
			break
	if count == 0:
		#num += 1
		total += i
		x.append(i)
		print i,
	count = 0
print total
