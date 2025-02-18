'''
#? 1 ] Define private attributes using double underscores (__).

#? 2 ] Create methods to interact with those private attributes.
'''

class Account:
    def __init__(self,balance = 0 ):
        self.__balance = balance

    def deposite(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if self.__balance >= amount : 
            self.__balance -= amount
        else :
            print('Insufficient funds')

    def get_balance(self):
        return self.__balance
    

pranav_account = Account(5000)

print(pranav_account.get_balance())

pranav_account.deposite(500)
print(pranav_account.get_balance())

pranav_account.withdraw(500)
print(pranav_account.get_balance())
pranav_account.withdraw(6000)


