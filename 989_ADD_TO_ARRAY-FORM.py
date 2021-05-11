a = [1, 2 , 0 ,5]
k = 34
i=-1
story = []
remainder = 0

while k > 0:
	o = k%10 + a[i] + remainder
	if o >= 10:
		story.append("9")
		remainder = 1
	else:
		story.append(o)
		


	


	'''
last_arr = a[i]
storx = k%10

var = curr_arr + storx
print(var)'''