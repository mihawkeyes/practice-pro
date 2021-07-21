#PF-Assgn-33

def find_common_characters(msg1,msg2):
    common_characters=''.join(a for a in msg1 if msg2.find(a)!=-1 and a!=' ') 
    if common_characters=='':
        return -1
    return common_characters
    #Remove pass and write your logic here

#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)