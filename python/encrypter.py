#PF-Assgn-47
def even(word):
    l=0
    vowel=('a','e','i','o','u','A','E','I','O','U')
    v,c,lst=[],[],[]
    wrd=list(word)
    if len(wrd)%2==0:
        while l<len(word):
            if wrd[l+1] in vowel:
                v.append(wrd[l+1])
            else:
                c.append(wrd[l+1])
            l+=2
    else:
        while l<len(word)-1:
            if wrd[l+1] in vowel:
                v.append(wrd[l+1])
            else:
                c.append(wrd[l+1])
            l+=2
    lst = c+v
    l,i=0,0
    if len(wrd)%2==0:
        while l<len(word):
            wrd[l+1]=lst[i]
            l+=2
            i+=1
    else:
        while l<len(word)-1:
            wrd[l+1]=lst[i]
            l+=2
            i+=1
    w=''.join(x for x in wrd)
    return w
def odd(word):
    l=0
    wrd = list(word)
    if len(wrd)%2==0:
        while l<len(word)//2:
            wrd[l],wrd[-l-2]=wrd[-l-2],wrd[l]
            l+=2
    else:
        while l<len(word)//2:
            wrd[l],wrd[-l-1]=wrd[-l-1],wrd[l]
            l+=2
    w=''.join(x for x in wrd)
    return even(w)


def encrypt_sentence(sentence):
    msg = sentence.split(' ')
    for word in msg:
        msg[msg.index(word)]= odd(word)
    ms = ''.join(x+' ' for x in msg)
    return ms
    #start writing your code here

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)