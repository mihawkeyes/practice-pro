#PF-Assgn-29
def calculate(distance,no_of_passengers):
    Price_per_litre= 70
    Mileage_of_bus_km_per_litre = 10
    Price_per_ticket = 80
    spending = distance/Mileage_of_bus_km_per_litre*Price_per_litre
    earning = no_of_passengers*Price_per_ticket
    if earning>spending:
        return earning-spending
    else :
        return -1
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))