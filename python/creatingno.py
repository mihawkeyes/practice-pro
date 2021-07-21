#PF-Assgn-36
def create_largest_number(number_list):
    new_list = sorted(number_list,reverse=True)
    largest_number=''.join([str(num) for num in new_list])
    return largest_number
    #remove pass and write your logic here

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)