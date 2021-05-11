def sumOddSubarr(arr):
	total=0
	suma=0
	for i in range(len(arr)):
		for j in range(i+1,len(arr)+1):
			x = arr[i:j]
			if len(x)%2!=0:
				#print(x)
				for k in range(i,j):
					suma+=arr[k]
				total+=suma
				suma=0
	return total 

arr = [1,4,2,5,3]
print(sumOddSubarr(arr))