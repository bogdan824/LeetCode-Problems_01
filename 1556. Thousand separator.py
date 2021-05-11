def thousandSep(n):
	x = str(n)
	if len(x)<=3:
		return x
	for i in range(len(x),0,-3):
		x = x[:i] + '.' + x[i:]
	return x[:-1]
n = 12345678912345678
print(thousandSep(n))