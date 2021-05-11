def longestCommonPrefix(strs):
	#if contains one or none, return the list
	if(len(strs))<2:
		return strs
	mini = len(min(strs))
	word = ""
	for i in range (len(strs[0][0:mini])):
		hold = strs[0][i]
		print()

		print("avem litera",hold)
		print("---")
		for j in range(1,len(strs)):
			print("o compar cu",strs[j][i],strs[j])
			if hold != strs[j][i]:
				return word
		word = strs[0][0:i+1]
		print("word este",word)

strs = [""]
#strs = ["cat","car","cas"]
#strs = ["dog","racecar","car"]
#strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))