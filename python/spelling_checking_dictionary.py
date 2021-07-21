#PF-Assgn-48

def find_correct(word_dict):
    contestent_spelling = word_dict.values()
    corret_spelling = word_dict.keys()
    result=[0]*3
    for spelling in corret_spelling:
        c=0
        c_spell_list=list(spelling)
        con_spell_list=list(word_dict[spelling])
        for s in range(0,len(c_spell_list)):
            if c_spell_list[s] == con_spell_list[s]:
                c+=1
        if c==len(c_spell_list):
            result[0]+=1
        elif c<len(c_spell_list)and c>=len(c_spell_list)-2:
            result[1]+=1
        else:
            result[2]+=1
    return result
    #start writing your code here

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))