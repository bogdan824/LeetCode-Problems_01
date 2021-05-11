def validPar(s):
	stack = []
	pairs = { "(" : ")", "[" : "]", "{" : "}"}
	for char in s:
		if char in pairs:
			stack.append(pairs[char])
		else:
			if len(stack)==0 or stack.pop()!=char:
				return False
	return len(stack)==0

s = "()"
print(validPar(s))