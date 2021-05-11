nums = [3,2,2,2,3,2,3]

val = 3
i = len(nums)
for i in range (len(nums)-1,-1,-1):
	print(nums[i])
	if nums[i] == val:
		nums.remove(nums[i])
		
print(len(nums),", nums =",str(nums))