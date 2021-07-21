#PF-Exer-26

def factorial(number):
    fact=1
    while number>0:
        fact*=number
        number-=1
    return fact
    #remove pass and write your logic to find and return the factorial of given number


def find_strong_numbers(num_list):
    new_list=[]
    for num in num_list:
        sum=0
        print(num)
        no = num
        while no>0:
            sum+=factorial(no%10)
            if sum>num:
                break
            no//=10
        if sum == num and num!=0:
            new_list.append(num)
     #remove pass and write your logic to find and return the list of strong numbers from the given list
    return new_list

num_list=[145, 375, 100, 2, 10, 40585, 0]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)