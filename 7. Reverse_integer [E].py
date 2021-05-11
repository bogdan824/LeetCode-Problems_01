'''
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit 
integer range [-231, 231 - 1], then return 0.
'''

def reverse(self, x: int) -> int:
    neg=1
    if x<0:
        neg = -1
        x=x*neg

    suma=0
    while x!=0:
        temp = x%10
        suma = (suma*10)+temp
        x=x//10   
    if suma < 2**31:
        suma = suma * neg 
        return suma
    else:
        return 0



