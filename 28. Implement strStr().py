def strstr(haystack,needle):
	x = len(needle)
	y = needle[0]

	if len(needle)==0:
		return 0

	for i in range (len(haystack)):
		if haystack[i] == y:
			sli = haystack[i:i+x]
			if sli == needle:
				return i
	return -1

haystack = "aaaaa"
needle	 = "bba"
print(strstr(haystack,needle))