#PF-Assgn-30
def encode(message):
    i=0
    k=1
    new_message = []
    while i<len(message)-1:
        if message[i]==message[i+1]:
            k+=1
        else:
            new_message.append(str(k)+message[i])
            k=1
        i+=1
    new_message.append(str(k)+message[i])
    encoded_message = ''.join(new_message)
    return encoded_message
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)