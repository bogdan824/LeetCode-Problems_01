def kidswithc(candies, extraCandies):
	maxi = -1
	keep = []
	for i in range (len(candies)):
		if candies[i]>maxi:
			maxi=candies[i]
	for candy in candies:
		if candy + extraCandies >= maxi:
			keep.append(True)
		else:
			keep.append(False)
	return keep
candies = [2,3,5,1,3]
extraCandies = 3
print(kidswithc(candies,extraCandies))