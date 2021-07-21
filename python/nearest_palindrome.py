#PF-Assgn-46
import math
def nearest_palindrome(number):
    no=list(str(number))
    for i in range(0,math.floor(len(no)/2)):
        no[-i-1]=no[i]
    n=''.join(x for x in no)
    number=n
    return number
    #start writitng your code here

number=12300
print(nearest_palindrome(number))