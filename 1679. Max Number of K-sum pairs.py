def maxOperation(nums,k):
	nums.sort()
	count = 0
	i = 0
	j = len(nums)-1

	while i<=j:
		if nums[i]+nums[j]==k:
			count+=1
			i+=1
			j-=1
		elif nums[i]+nums[j]>k:
			j-=1
		else:
			i+=1
	return count


nums = [1,2,3,4,5,6,7]
k = 5
print(maxOperation(nums,k))