#PF-Assgn-39
#This verification is based on string match.     

#Global variables
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,250,3]

'''This method accepts the item followed by the quantity required by a customer in the format item1, quantity_required, item2, quantity_required etc.'''
def place_order(*item_tuple):
    item=0
    #Remove pass and write your logic here
    while item in range(0,len(item_tuple)):
        if item_tuple[item] in menu:
            print(item_tuple[item],"is  available")
            if check_quantity_available(menu.index(item_tuple[item]),item_tuple[item+1]):
                print(item_tuple[item],"stock is over")
        else:
            print(item_tuple[item],"is not available")
        item+=2

    #Populate the item name in the below given print statements
    #Use it to display the output wherever applicable
    #Also, do not modify the text in it for verification to work
    
    #print("<item name>is not available")
    #print("<item name>stock is over")
    #print ("<item name>is available")
    
  


'''This method accepts the index position of the item requested by the customer in the quantity_available list, and the requested quantity of the item.'''
def check_quantity_available(index,quantity_requested):
    global quantity_available
    if quantity_available[index]<quantity_requested:
        return 1
    else:
        quantity_available[index] -= quantity_requested
    #Remove pass and write your logic here to return an appropriate boolean value.


#Provide different values for items ordered and test your program
place_order("Veg Roll",2,"Noodles",2)
place_order("Soup",1,"Veg Roll", 2, "Fried Rice1",1)