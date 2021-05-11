def countItems(items, ruleKey, rukeValue):
	count = 0
	if ruleKey == "type":
		x = 0
	elif ruleKey == "color":
		x = 1
	else:
		x = 2
	
	for i in range (len(items)):
		if items[i][x] == ruleValue:
			count+=1
	return count


items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

print(countItems(items,ruleKey,ruleValue))