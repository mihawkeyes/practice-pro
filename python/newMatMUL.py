import math
a=[[1,2],[3,4]]
b=[[0,5],[6,7]]
c=[]
# print(len(a))
for i in range(len(a)*2):
    temp=[]
    for j in range(len(b)*2):
        # print(i//2,j//2,i%2,j%2)
        temp.append(a[i//2][j//2]*b[math.floor(int(i%2))][math.floor(int(j%2))])
    c.append(temp)
    # print()

for i in range(len(a)*2):
    # for j in range(len(b)*2):
    #     print(c[i][j],end=" ")
    print(c[i])