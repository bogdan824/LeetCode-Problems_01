#CONVERT ROMAN NUMBERS TO INTEGERS
s = "IV"

#1. Store all the numbers in a dictionary;
dic = { 'I':1, 'V':5 , 'X':10 , 'L':50, 'C':100 , 'D':500, 'M':1000}

#2. Take 2 values: prev = 0 & cur = 0. Keep track: total = 0
prev = cur = total = 0

#3. Loop through the string
for i in range (len(s)):
    cur = dic[s[i]]
    if cur > prev:
        total = total + cur - 2 * prev
    else:
        total += cur
    prev = cur
print(total)