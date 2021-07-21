#PF-Assgn-58 Luhn algorithm to validate a credit card number.
def validate_credit_card_number(card_number):
    odd,even,add=0,0,0
    card_num=list(str(card_number))
    for i in range(0,len(card_num)):
        if i%2==0:
            temp=int(card_num[i])*2
            if (temp)>9:
                digits=list(str(temp))
                sum=0
                for i in digits:
                    sum+=int(i)
                odd+=sum
            odd+=temp
        else :
            even+=int(card_num[i])
    add=even+odd
    return add%10==0
    #start writing your code here

card_number= 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")