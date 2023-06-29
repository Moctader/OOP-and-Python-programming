class Resturant:
    def __init__(self, name, rent,  menu=[]) -> None:
        self.name=name
        self.orders=[]
        self.chef=None
        self.server=None
        self.manager=None
        self.rent=rent
        self.menu=menu
        self.revenue=0
        self.profit=0
        self.balance=0
        self.expense=0

    def add_employee(self, employess_type, employee):
        if employess_type=='chef':
            self.chef=employee

        elif employess_type=='server':
            self.server=employee
        
        elif employess_type=='manager':
            self.manager=employee
    
    def add_order(self, order):
        self.orders.append(order)

    def recive_payment(self,order,  amount, customer):
        print(amount, order.bill)
        if amount>=order.bill:
            self.revenue+=order.bill
            self.balance+=order.bill
            customer.due_amount=0
            return amount-order.bill
        else:
            print("Not enough money pay more")

    def pay_expanse(self, amount, description):
        if amount<self.balance:
            self.expense+=amount
            self.balance-=amount
            print(f'expanse{amount} for {description}')
        else:
            print(f'Not enough money to pay{amount}')

    def pay_salary(self, employee):
        print(f'paying salary for {employee.name} salary: {employee.salary}')
        if employee.salary<self.balance:
            self.balance-=employee.salary
            self.expense+=employee.salary
            employee.recive_salary()


    def show_employess(self):
        if self.chef is not None:
            print(f'chef: {self.chef.name} with salary: {self.chef.salary}')

    def show_employee(self):
        if self.chef is not None:
            print(f'chef: {self.chef.name} with salary: {self.chef.salary}')
    