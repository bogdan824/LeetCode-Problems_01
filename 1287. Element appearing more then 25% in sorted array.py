def findNum(arr):
	hashm = {}
	for i in arr:
		if i in hashm:
			hashm[i]+=1
		else:
			hashm[i]=1
	for k,v in hashm.items():
		if v>len(arr)/4:
			return k
		

arr = [1,2,2,6,6,6,6,7,10]
print(findNum(arr))