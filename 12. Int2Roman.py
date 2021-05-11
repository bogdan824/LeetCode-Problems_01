#1. Create a dictionary to hold the values
#dic = { '1':I,'4':IV,'5':V,'9':IX,'10':X,'40':XL,'50':L,'90':XC,'100':C,'400':CD,'500':D,'900':CM,'1000':M}
def int2rom(num):
	numbs = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
	roms  = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
	i = len(numbs)-1
	keep = ''

	while num != 0:
		if num >= numbs[i]:
			keep+=roms[i]
			num-=numbs[i]
		else: i-=1
	return keep

print(int2rom(99))