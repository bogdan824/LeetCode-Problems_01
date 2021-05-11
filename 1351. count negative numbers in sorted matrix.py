def countNeg(grid):
	count = 0
	for i in range (len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] < 0:
				count+=1
	return count

#grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
#grid = [[5,1,0],[-5,-5,-5]]
grid = [[3,2],[1,0]]
print(countNeg(grid))