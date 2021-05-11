'''
You are given a string allowed consisting of distinct characters and an array of strings words. 
A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.
'''
def countStrings(allowed,words):
	allowed = set(allowed)
	count = 0 

	for word in words:
		for letter in word:
			if letter not in allowed:
				count += 1
				break
	return len(words)-count



allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(countStrings(allowed,words))