i=999
while i >= 900:
	for j in range (0,100):
		x = i*(i-j)
		if x%10 == x/100000:
			if (x%100)/10 == (x/10000)%10:
				if (x%1000)/100 == (x/1000)%10:
					print i, i-j, x
					break
	i -= 1
