"""class Customer():
    def __init__(self,name):
        self.customer_name=name
        self.bill_amount=1000
    def pays_bill(self,amount):
        print(self.customer_name+' pays bill amount of Rs. '+amount)
    def purchase(self):
        self.discounted_bill=self.bill_amount-self.bill_amount*0.05
        self.pays_bill(str(self.discounted_bill))


customer1=Customer('ruthvik')
customer1.purchase()"""


    def __init__(self,id,vtype,cost):
        self.__vehicle_id=id
        self.__vehicle_type=vtype
        self.__vehicle_cost=cost
        if self.__vehicle_type=="Two Wheeler":
            self.__premium_amount=self.__vehicle_cost*0.02
        elif self.__vehicle_type=="Four Wheeler":
            self.__premium_amount=self.__vehicle_cost*0.06
        else:
            self.__premium_amount=None
    def get_vehicle_detalis(self):
        print('vehicle id: '+str(self.__vehicle_id))
        print('vehicle cost: '+str(self.__vehicle_cost))
        if self.__vehicle_type=="Two Wheeler":
            print('vehicle type: '+self.__vehicle_type)
            print('premium amount: '+str(self.__premium_amount))
        elif self.__vehicle_type=="Four Wheeler":
            print('vehicle type: '+self.__vehicle_type)
            print('premium amount: '+str(self.__premium_amount))

    def set_vehicle_detalis(self,vtype,cost):
        self.__vehicle_type=vtype
        self.__vehicle_cost=cost
        if self.__vehicle_type=="Two Wheeler":
            self.__premium_amount=self.__vehicle_cost*0.02
        elif self.__vehicle_type=="Four Wheeler":
            self.__premium_amount=self.__vehicle_cost*0.06
        else:
            self.__premium_amount=None
        


customer1=Vehicle(100,'Two Wheeler',200000)
customer1.get_vehicle_detalis()
customer1.set_vehicle_detalis("Four Wheeler",200000)
customer1.get_vehicle_detalis()