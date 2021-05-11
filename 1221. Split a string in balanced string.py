def balancedString(s):
	keep=0
	stor=0
	for i in range (len(s)):
		if s[i]=="L":
			keep-=1
		if s[i]=="R":
			keep+=1
		if keep == 0:
			stor+=1
	return stor


s = "RLRRLLRLRL"
print(balancedString(s))