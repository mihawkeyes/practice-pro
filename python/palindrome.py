#PF-Assgn-40
def is_palindrome(word):
    if word[0]==word[-1] :
        if len(word)!=0:
            word.replace(word[0],'')
            word.replace(word[-1],'')
            is_palindrome(word)
        else:
            return True
    else:
        return False
    
    
    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")