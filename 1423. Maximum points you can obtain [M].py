'''
There are several cards arranged in a row, and each card has an associated number
of points The points are given in the integer array cardPoints.
In one step, you can take one card from the beginning or from the end of the row.
You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
'''

def maxScore(cardPoints,k):
	maxi = 0
	a = 0
	b = k

	while k>0 or a <= b:
		i = cardPoints[0:k]
		j = cardPoints[len(cardPoints)-a:len(cardPoints)]
		suma = (sum(i)) + (sum(j))
		k-=1
		a+=1
		if suma > maxi:
			maxi = suma

cardPoints = [5,4,-1,4,2,-2,1,6]	
#cardPoints = [1,2,3,4,5,6,1] #k=3
#cardPoints = [100,40,17,9,73,75] #k=3
k = 4
print(maxScore(cardPoints,k))