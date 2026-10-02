class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
    
my_account = BankAccount(1000)
print(my_account.get_balance())