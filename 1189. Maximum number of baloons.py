def maxNumb(text):
	keep = {"b":0,"a":0,"l":0,"o":0,"n":0}
	for i in range(len(text)):
		if text[i] in keep:
			keep[text[i]]+=1
			#print(text[i])
			#print(keep)
	#print(keep)
	x = (keep["l"])
	keep["l"]=x//2
	x = (keep["o"])
	keep["o"]=x//2
	#print(keep)
		#print("---")
	return(min(keep.values()))

text = "nlaebolko"
print(maxNumb(text))