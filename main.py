class Account():
    count=0
    @classmethod
    def incr_count(cls):
        cls.count+=1

    @classmethod
    def get_count(cls):
        return cls.count

    def __init__(self,Cust_id,name,initial_balance=0):
        self.__id = Cust_id
        self.__name=name
        self.__balance=initial_balance
        Account.incr_count()

    def get_balance(self):
        return self.__balance
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name



    def  deposite(self,amount):
        self.__balance = self.__balance+amount
        return self.__balance

    def withdrow(self,withdraw):
        self.__balance = self.__balance-withdraw
        return self.__balance


customer1 = Account("101","ABC")

print(customer1.deposite(5000))

customer1.withdrow(200)

print(customer1.get_id(),customer1.get_name(),customer1.get_balance())

# customer1.balance=30000
print(customer1.get_balance())



print(Account.get_count())
Account.incr_count()
Account.incr_count()
print(Account.get_count())


class saving_Account(Account):
    def __init__(self,id,name,initial_balance=0):
        super().__init__(id,name,initial_balance)
        self.__limit = 50000

    def withdrow(self,amount):
        if amount<self.__limit:
            new_bal = super().withdrow(amount)
            self.__limit-=amount
        else:
            print("You reaches daily limit")
        return new_bal


cust1 = saving_Account(101,"abcv")
# print(cust1.__limit)

print(cust1.deposite(80000))
print(cust1.withdrow(40000))
print(cust1.withdrow(40000))
