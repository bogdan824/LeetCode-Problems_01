def distVal(arr1,arr2,d):
	count = 0
	for i in range (len(arr1)):
		y = True
		for j in range (len(arr2)):
			x = arr1[i] - arr2[j]
			if x < 0:
				x*=-1
			print("x =",x)
			if not  x > d:
				y = False
		if y == True:
			count+=1
		print("count",count)
	return count

arr1 = [1,4,2,3]
arr2 = [-4,-3,6,10,20,30]
d = 3
print(distVal(arr1,arr2,d))