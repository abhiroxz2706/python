class computer:
    def __init__(self):
        self.__maxprice=500
    def sell(self):
        print("sellling price:",self.__maxprice)
    def newsell(self,price):
        self.__maxprice=price
    
obj=computer()
obj.sell()
obj.__maxprice=1000
obj.sell()
obj.newsell(1000)
obj.sell()