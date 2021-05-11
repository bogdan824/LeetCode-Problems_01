def howMany(nums):
	keep = []
	for i in range(len(nums)):
		count = 0
		for j in range(len(nums)):
			if nums[j]<nums[i]:
				count+=1
		keep.append(count)
	return keep


#nums = [8,1,2,2,3]
nums = [6,5,4,8]

print(howMany(nums))