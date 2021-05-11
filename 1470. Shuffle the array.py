def shuffArray(nums,n):
	keep = []
	for i in range(n):
		j=i+n
		keep.append(nums[i])
		keep.append(nums[j])
	return keep


nums = [1,1,2,2]
n = 2
print(shuffArray(nums,n))