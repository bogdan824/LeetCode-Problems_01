'''
You are given coordinates, a string that represents the coordinates of a square of the chessboard
Below is a chessboard for your reference.
Return true if the square is white, and false if the square is black.
The coordinate will always represent a valid chessboard square.
The coordinate will always have the letter first, and the number second.
'''

def squareWhite(coordinates):
	keep = ["x","a","b","c","d","e","f","g","h"]
	y = coordinates[1]
	if coordinates[0] in keep:
		x = keep.index(coordinates[0])
	if (x+int(y))%2!=0:
		return True
	return False 




coordinates = "c7"
print(squareWhite(coordinates))