'''
Given numBottles full water bottles, you can exchange numExchange empty water
bottles for one full water bottle.
The operation of drinking a full water bottle turns it into an empty bottle.
Return the maximum number of water bottles you can drink.
'''

def numOfBottles(numBottles,numExchange):
	total = numBottles
	#print("numBottles",numBottles)
	#print("numExchange",numExchange)

	while numBottles >= numExchange:
		x = numBottles%numExchange
		numBottles = numBottles//numExchange
		total += numBottles
		numBottles+=x
	#total+=numBottles%numExchange
	return total

numBottles = 9
numExchange = 3
print(numOfBottles(numBottles,numExchange))
