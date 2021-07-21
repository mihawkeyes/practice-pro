def GCD(num1,num2):
    if num1==num2 or num1%num2==0:
        return num2
    if num2%num1==0:
        return num1
    if num1>num2:
        return GCD(num1%num2,num2)
    if num2>num1:
        return GCD(num1,num2%num1)

def gcd(a,b):
    while(b!=0):
        t=a
        a=b
        b=t%b

    return a
print(gcd(int(input("enter first number: ")),int(input("enter second value: "))))