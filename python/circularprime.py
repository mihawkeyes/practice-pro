#PF-Assgn-57
#Assume n = 123.
#Multiply n with 10 i.e. n = n * 10 = 1230.
#Add the first digit to the resultant number i.e. 1230 + 1 = 1231.
#Subtract (first digit) * 10k from the resultant number where k is the number of digits in the original number (in this case, k = 3).
#1231 – 1000 = 231 is the left shift number of the original number.
def check_prime(number):    
    half=number//2
    while half>0:
        if half == 1 :
            return True
        elif number%half==0:
            return False
        else:
            half-=1 #remove pass and write your logic here. if the number is prime return true, else return false

def rotations(num):
    no = [x for x in str(num)]
    powten = 10 ** (len(no))
    n=num
    for x in range(0,len(no)) :
        n = n*10+int(no[x])-(powten*int(no[x]))
        no[x] = n
        n=no[x]
    return set(no)
    #remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
	#Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]

def get_circular_prime_count(limit):
    prime=[]
    circular_prime=set()
    for number in range(2,limit):
        if check_prime(number):
            prime.append(number)
    for number in range(0,len(prime)):
        if prime[number] >=10 :
            count=0
            temp=rotations(prime[number])
            t=len(temp)
            for n in temp:
                if check_prime(n):
                    count+=1
            if count == t :
                for n in temp:
                    if  n<=limit:
                        circular_prime.add(n)
        else:
            circular_prime.add(prime[number])
    circular_prime_list = list(circular_prime)
    return sorted(circular_prime_list)


    #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.
print(get_circular_prime_count(1000))
#Provide different values for limit and test your programprint(get_circular_prime_count(50))