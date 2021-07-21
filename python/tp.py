# #PF-Assgn-34
# def find_pairs_of_numbers(num_list,n):
#     sum=0
#     for num in num_list:
#         for no in range(num_list.index(num),len(num_list)):
#             if num+num_list[no]==n:
#                 sum+=1
#     return sum
#     #Remove pass and write your logic here

# num_list={'ruthvik','suresh','vachhani'}
# for i in num_list:
#     print(i)
# print(type(num_list))

def main():
    s = input()
    mom=[]
    dad=[]
    for i in s:
        if i == 'M' or (i == 'O' and mom[0]=='M'):
            mom.append(i)
        if i == 'D' or (i == 'A' and dad[0]=='D'):
            dad.append(i)
    
    no_of_o = 0
    no_of_mom = 0
    no_of_a = 0
    no_of_dad = 0
    for i in range(len(mom)-1,0,-1):
        if mom[i] == 'M':
            break
        mom.pop()

    for i in range(len(dad)-1,0,-1):
        if dad[i] == 'D':
            break
        dad.pop()

    i=1
    while i < len(mom)-1:
        while mom[i] == 'O':
            no_of_o += 1
            i+=1
        i+=1
        no_of_mom += no_of_mom + no_of_o
    print(no_of_mom)

    i=1
    while i < len(dad)-1:
        while dad[i] == 'A':
            no_of_a += 1
            i+=1
        i+=1
        no_of_dad += no_of_dad + no_of_a
    print(no_of_dad)
    # for i in mom:
    #     print(i)

    # for i in dad:
    #     print(i)

main()