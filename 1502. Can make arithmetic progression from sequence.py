def arrPro(arr):
	arr.sort(reverse=True)
	arr.append(0)
	
	x = arr[0] - arr[1]
	
	for i in  range (1,len(arr)-2):
		if arr[i]-arr[i+1] != x:
			return False
	return True


arr = [1,2,4]
print(arrPro(arr))