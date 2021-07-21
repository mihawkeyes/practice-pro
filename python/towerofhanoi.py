def TOH(n,source,temp,destination):
    if n==1:
        print(f"move {n} from {source} to {destination}")
        return
    # print(destination)
    TOH(n-1, source, destination, temp)
    # destination[n-1] = source[n-1]
    print(f"move {n} from {source} to {destination}")
    TOH(n-1, temp, source, destination)
n=int(input('Enter no of rings to shift: '))
# source=[0]*n
# temp=[0]*n
# destination=[0]*n
# for x in range(0,n) :
#     source[x]=input('enter the colour of ring from smaller to bigger: ')
TOH(n,'A','B','C')

