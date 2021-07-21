def fabonacci(term):
    if term <= 2 :
        return 1
    else:
        return fabonacci(term-1)+fabonacci(term-2)

print(fabonacci(int(input('enter term to find in fabonacci serise: '))))