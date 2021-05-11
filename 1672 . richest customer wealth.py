def richCust(accounts):
	maxi = 0
	for i in range(len(accounts)):
		suma = 0
		for j in range(len(accounts[i])):
			suma += accounts[i][j]
			if suma > maxi:
				maxi =suma
	return maxi



accounts = [[1,2,3],[3,2,]]
print(richCust(accounts))