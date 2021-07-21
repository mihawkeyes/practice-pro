#PF-Assgn-60
def remove_duplicates(value):
    val=''.join(value[0])
    for i in range(1,len(value)):
        if value[i] in val:
            pass
        else:
            val+=value[i] 
    return val
    #start writing your code here
print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))