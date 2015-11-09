l = []
sam = []
total = 1
for i in range (2, 21):
	""" find common divisible numbers """
	for j in range (2,i+1):
		if i%j == 0:
			sam.append(j)

	if total%i != 0:
		for j in sam:
			if (total * j) % i == 0:
				total = total * j
				break
	print sam
	sam = []

print total
