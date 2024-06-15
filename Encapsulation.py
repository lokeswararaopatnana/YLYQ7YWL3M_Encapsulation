class BankAccount:
    def __init__(self, owner, balance,secret_key):
        self.owner = owner
        self.__balance = balance
        self.__secret_key = secret_key
    
    def __show_details(self):
        print("Account Owner:",self.owner)
        print("Account Balance:",self.__balance)
        
    def check_balance(self,provided_secret_key):
        if self.__secret_key == provided_secret_key:
            self.__show_details()
        else:
            print("Invalid Secret Key!!!")
        
    def get_balance(self):
        return self.__balance
        
    def set_balance(self,balance,provided_secret_key):
        if self.__secret_key == provided_secret_key:
            self.__balance = balance
        else:
            print("Invalid Secret Key!!!")
        
account = BankAccount("Lokesh",50000,"1202")
print("Account Balance:",account.get_balance())
account.set_balance(80000,"1202")
print("Updated Balance:",account.get_balance())
account.check_balance("1202")