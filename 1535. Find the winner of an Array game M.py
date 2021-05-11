def findWinner(arr,k):
	if k>len(arr):
		return max(arr)
	first_val = arr[0]
	win_count = 0
	while win_count!=k:
		if arr[0] > arr[1]:
			arr.append(arr[1])
			arr.remove(arr[1])
		else:
			arr.append(arr[0])
			arr.remove(arr[0])
			win_count=0
		first_val = arr[0]
		win_count+=1
	return arr[0]
	
		


#arr = [2,1,3,5,4,6,7]
#k = 2
arr = [1,25,35,42,68,70]
k = 1
print(findWinner(arr,k))