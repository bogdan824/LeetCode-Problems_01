def maxProd(nums):
	maxi = 0
	for i in range (len(nums)-1):
		for j in range (i+1,len(nums)):
			x = ((nums[i]-1)) * ((nums[j]-1))
			if x > maxi:
				maxi = x
	return maxi
nums = [3,4,5,2]
print(maxProd(nums))