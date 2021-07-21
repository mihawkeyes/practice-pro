#PF-Assgn-59
def check_perfect_number(number):
    perfect_divisor=[]
    for i in range(1,number):
        if number%i==0:
            perfect_divisor.append(i)
    if sum(perfect_divisor)==number:
        return True
    else:
        return False
    #start writing your code here

def check_perfectno_from_list(no_list):
    new_no_list=[]
    for i in range(0,len(no_list)):
        if check_perfect_number(no_list[i]) and no_list[i]!=0:
            new_no_list.append(no_list[i])
    return new_no_list
    #start writing your code here

perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)