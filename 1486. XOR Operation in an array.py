def xorOperation(n,start):
	ans = 0
	for i in range(n):
		ans = start + 2*i
	return ans

n = 5
start = 0
print(xorOperation(n,start))