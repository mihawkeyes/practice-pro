#PF-Assgn-50

def sms_encoding(data):
    vowel=['A','E','I','O','U','a','e','i','o','u']
    sms=data.split(' ')
    for letter in sms:
        word=list(letter)
        for l in word:
            if l not in vowel:
                for x in word:
                    if x in vowel:
                        word.remove(x)
                break
        w=''.join(x for x in word)
        sms[sms.index(letter)]=w
    msg=''.join(x+' ' for x in sms)
    return msg

    #start writing your code here

data="I love Python"
print(sms_encoding(data))