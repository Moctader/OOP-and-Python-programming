class bank:

    def __init__(self, balance):
        self.balance=balance
        self.min_withdraw=100
        self.max_withdraw=100000

    def get_balance(self):
        return self.get_balance
    
    def deposit(self, amount):
        if amount >0:
            self.balance+=amount

    def withdraw(self, amount):
        if amount<100:
            print(f'you can not withdraw less than {self.min_withdraw}')
        elif amount>self.max_withdraw:
            print(f'you can not withdraw more than {self.max_withdraw}')
        else:
            self.balance-=amount
            print(f'withdraw amount {amount}')
            print(f'Remaining balance is {self.balance}')


brac=bank(15000)
brac.deposit(2000)
brac.withdraw(90)
brac.withdraw(1000000)
brac.withdraw(1000)