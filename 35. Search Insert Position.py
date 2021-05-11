#Given a sorted array of distinct integers and a target value, return the index if the target is found.
#If not, return the index where it would be if it were inserted in order.
def insert_pos(nums,target):
	for i in range (len(nums)):
		if nums[i]==target:
			return i
	d = 0
	for j in range(len(nums)):
		if target > nums[j]:
			d=j+1
	return d
	
nums = [1,3,5,6]
target = 7
print(insert_pos(nums,target))