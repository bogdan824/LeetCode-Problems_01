def goodPairs(nums):
	count = 0
	for i in range(len(nums)-1):
		for j in range(i+1, len(nums)):
			if nums[i] == nums[j] and i<j:
				count+=1
	return count

nums = [1,2,3,1,1,3]
print(goodPairs(nums))