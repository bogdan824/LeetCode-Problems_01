def strAlike(s):
	ct_a = 0
	ct_b = 0
	vowels = ('a','e','i','o','u','A','E','I','O','U')
	a = s[0:len(s)//2]
	b = s[len(s)//2:]
	for i in range (len(b)):
		if a[i] in vowels:
			ct_a += 1
		if b[i] in vowels:
			ct_b += 1
	if ct_a == ct_b:
		return True
	return False


s = "textbook"
print(strAlike(s))