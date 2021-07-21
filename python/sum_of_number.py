#PF-Assgn-52

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    if filter_func!=None:
        data = filter_func(list_of_num) 
    else:
        data = list_of_num
    sum=0
    for x in data :
        sum += x
    return sum

#Remove pass and write the logic here

def even(data):
    even_data=[]
    for x in data:
        if x%2==0:
            even_data.append(x)
    return even_data

def odd(data):
    odd_data=[]
    for x in data:
        if x%2!=0:
            odd_data.append(x)
    return odd_data
#Remove pass and write the logic here

sample_data = range(1,11)
print(sum_of_numbers(sample_data,None))
print(sum_of_numbers(sample_data,even))
print(sum_of_numbers(sample_data,odd))