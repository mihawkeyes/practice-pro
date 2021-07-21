p = int(input("enter no of row. "))
for x in range(1,p+1) :
	for y in range(1,p*2+1) :
		if y<=p:
			if y<=p-x+1: 
				print("*",end="")
			else :
				print(" ",end="")
		if y>p:	
			if y-p>=x :
				print("*",end="")
			else :
				print(" ",end="")
	print()
for x in range(1,p+1):
	for y in range(1,p*2+1) :
		if y<=p:
			if y<=x: 
				print("*",end="")
			else :
				print(" ",end="")
		if y>p:	
			if y-p>p-x :
				print("*",end="")
			else :
				print(" ",end="")
	print()