def maxLengh(arr):
	stor = []
	stor.append("")
	for a in range (len(arr)):
		stor.append(arr[a])
	for i in range (len(arr)-1):
		for j in range (1,len(arr)):
			if arr[i] != arr[j]:
				stor.append(arr[i]+arr[j])
	maxi = ""
	for b in range (len(stor)):
		if (len(stor[b])) > len(maxi):
			maxi = stor[b]
	return len(maxi)

arr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
#arr = ["abcdefghijklmnopqrstuvwxyz"]	
#arr = ["cha","r","act","ers"]
#arr = ["un","iq","ue"]
print(maxLengh(arr))

