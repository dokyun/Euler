total = 0
ind = 0
for i in range(1,101):
	total += i
	ind += i**2
total = total**2
print total, ind, total-ind
