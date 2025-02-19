# Create a BankAccount class with deposit/withdraw methods.
class Account:
    def __init__(self,accno,name,phone,balance):
        self.__accno=accno
        self.__name=name
        self.__phone=phone
        self.__balance=balance
    def getbalance(self):
        return self.__balance
    def setbalance(self,balance):
        self.__balance=balance
user1=Account(22,"Sachin",333443,0)
user2=Account(32,"rohit",3435454545,1000)
print(user1.getbalance())
user1.setbalance(6666)
print(user1.getbalance())

