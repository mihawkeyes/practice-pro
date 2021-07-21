grocery=['butter','bread','milk','eggs']
ava=['butter','milk','eggs','bread','chips']
total=0
price=[50,60,20,30,10]
for item in grocery:
    if item in ava:
        total+=price[ava.index(item)]
print(total)