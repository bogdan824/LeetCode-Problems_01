def genString(n):
	word = ""
	if n%2==0:
		for i in range (n-1):
			word += "a"
		word += "b"
	else:
		for i in range (n):
			word += "a"
	return word

n = 4
print(genString(n))