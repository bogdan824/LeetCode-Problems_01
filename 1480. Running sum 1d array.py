
nums = [1,2,3,4]
suma = 0
for i in range (len(nums)):
	nums[i]=nums[i]+suma
	suma=nums[i]
print(nums)
