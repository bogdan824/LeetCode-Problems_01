def sumOfElem(nums):
	hashm = {}
	for i in nums:
		if i in hashm.keys():
			hashm[i] +=1
		else:
			hashm[i] = 1
	suma = 0

	for k,v in hashm.items():
		if v == 1:
			suma += k
	return suma


nums = [1,2,3,2]
print(sumOfElem(nums))