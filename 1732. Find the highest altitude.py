def largestAltitude(gain):
	keep = [0]
	for x in range (len(gain)):
		#keep.append(keep[x]+suma[x])
		keep.append(keep[-1]+gain[x])
	return max(keep)

gain = [-5,1,5,0,-7]
print(largestAltitude(gain))