'''
A good meal is a meal that contains exactly two different food items with a sum
of deliciousness equal to a power of two.
You can pick any two different foods to make a good meal.
Given an array of integers deliciousness where deliciousness[i] 
is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different 
good meals you can make from this list modulo 109 + 7.
Note that items with different indices are considered different even if they have the same deliciousness value.
'''
def countMeals(deliciousness):
	keep = []
	count = 0
	for i in range (22):
		keep.append(2**i)

	for i in range(len(deliciousness)-1):
		for j in range (i+1,len(deliciousness)):
			if deliciousness[i]+deliciousness[j] in keep:
				count+=1
	return count


#deliciousness = [149,107,1,63,0,1,6867,1325,5611,2581,39,89,46,18,12,20,22,234]
#deliciousness = [1,1,1,3,3,3,7]
deliciousness = [1,3,5,7,9]
print(countMeals(deliciousness))