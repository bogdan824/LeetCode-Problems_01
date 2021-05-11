def decompress(nums):
	keep = []
	for i in range (0,len(nums),2):
		x = nums[i]
		while x > 0:
			keep.append(nums[i+1])
			x-=1
	return keep



#nums = [1,2,3,4]
nums = [1,1,2,3]
print(decompress(nums))