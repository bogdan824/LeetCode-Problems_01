nums = [0,0,1,1,1,2,2,2,3,3,4,4]
i = len(nums)-1

#nums = [1,1,2]

while i > 0:
	if nums[i] == nums [i-1]:
		nums.remove(nums[i-1])
	i-=1
print(str(len(nums))+ ", nums = " + str(nums))