class bank:

    def __init__ (self, balance):
        self.balance=balance
        self.min_withdrae=100
        self.max_withdrae=100000

    def get_balance(self):
        return self.get_balance
    
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
    

    def withdraw(self, amount):
        if amount<self.min_withdrae:
            print(f'you can not withdraw less than {self.min_withdrae}')
        elif amount>self.max_withdrae:
            print(f'you can not withdraw more than {self.max_withdrae}')
        else:
            self.balance-=amount
            print(f'withdaw amount {amount}')
            print(f'current balance {self.balance}')

    

brac=bank(15000)
brac.deposit(200000)
brac.withdraw(50)
brac.withdraw(500000000000)
brac.withdraw(1000)