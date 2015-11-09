lis = [1, 2]
i = 0;
while lis[i] + lis[i+1] < 4000000:
	lis.append(lis[i] + lis[i+1])
	i += 1

total = 0
for x in lis:
	if x%2 == 0:
		total += x
print total
