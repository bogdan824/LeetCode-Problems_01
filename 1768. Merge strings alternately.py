def mergeStrings(word1,word2):
	store = ""
	mini = min(len(word1),len(word2))

	for i in range (mini): 
		store += word1[i]
		store += word2[i]

	if word1[mini:]:
		store += word1[mini:]
	if word2[mini:]:
		store += word2[mini:]

	return store
	
word1 = "abc"
word2 = "pqrgg"
print(mergeStrings(word1,word2))