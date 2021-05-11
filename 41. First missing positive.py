def firstPos(nums):
	nums.sort()
	while nums[0]<1:
		if nums[0] is None:
			return 1
		del nums[0]
	if len(nums) < 1:
		return 1
	if nums[0]==0 and len(nums)==1:
		return 1

	for i in range(len(nums)):
		if nums[i]!=i+1:
			return i+1
	return nums[-1]+1
nums = [-5]
#nums = [3,4,-1,1]
#nums = [1,2,0]
#nums = [7,8,9,11,12]
print(firstPos(nums))