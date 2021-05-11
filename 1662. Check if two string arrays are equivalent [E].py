'''
Given two string arrays word1 and word2, return true if the two arrays represent the same string,
and false otherwise.
A string is represented by an array if the array elements concatenated in order forms the string.
'''
def checkArr(word1,word2):
	sumw1 = ""
	sumw2 = ""
	for i in word1:
		sumw1+=i
	for j in word2:
		sumw2+=j	

	if sumw1 == sumw2:
		return True
	return False

word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(checkArr(word1,word2))