def find_ten_substring(num_str):
    m=[]
    l=[]
    for i in range(0,len(num_str)):
        for j in range(i,len(num_str)):
            m.append(num_str[i:j+1])       
    for k in set(m):
        s=0
        for b in range(0,len(k)):
            s=s+int(k[b])
            if(s==10 and b+1==len(k)):
                l.append(k)
    return l
    #Remove pass and write your logic here

num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)