def numbStud(startTime,endTime,queryTime):
	count = 0
	for i in range(len(startTime)):
		if queryTime>=startTime[i] and queryTime<=endTime[i]:
			count+=1

	return count

startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4
print(numbStud(startTime,endTime,queryTime))