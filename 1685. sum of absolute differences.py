def absoluteSum(nums):
	#for i in range(len(nums)):
	#	if nums[i] < 0:
	#		nums[i]*=-1
	#		print("nums sunt",nums)
	keep = []
	suma = 0
	for num1 in nums:
		for num2 in nums:
			x = num1 - num2
			if x < 0:
				x*=-1
			suma+=x
		keep.append(suma)
		suma=0
	return keep




nums = [2, 3, 5]
print(absoluteSum(nums))