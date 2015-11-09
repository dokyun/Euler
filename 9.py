for a in range(1,500):
	if a%2 == 0:
		b = (1000-a)/2
		c = 1000-a-b
	else:
		b = (1000-a)/2+1
		c = 1000-a-b

	while b**2 < a**2 + c**2:
		b += 1
		c -= 1

	if b**2 == a**2 + c**2:
		print b, a, c, b**2, a**2, c**2
		print a*b*c
		break
