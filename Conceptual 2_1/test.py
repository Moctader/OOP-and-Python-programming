class product:
    def __init__(self, name, price, quantity) -> None:
        self.product_name=name
        self.product_price=price
        self.product_quantity=quantity

class store:
    def __init__(self) -> None:
        self.product_price_dic={}
        self.product_quantity_dic={}
        self.profit=0

    def add_product(self, name, price, quantity):
        pro_duct=product(name, price, quantity)
        self.product_price_dic[pro_duct.product_name]=pro_duct.product_price
        self.product_quantity_dic[pro_duct.product_name]=pro_duct.product_quantity

    def buy_product(self, name, quantity):
        if name in self.product_price_dic:
            if  self.product_quantity_dic[name]<quantity:
                print('Not available')
            else:
                self.product_quantity_dic[name]=self.product_quantity_dic[name]-quantity
                #profit
                self.profit=((5*self.product_price_dic[name])/100)*quantity
                print('Thank you')
        else:
            print('Not found')
        
    def show_product(self):
        print(f'products are {self.product_price_dic} & {self.product_quantity_dic}')

    def show_profit_amount_left(self):
        print(f'profit {self.profit}')


class shop(store):
    def __init__(self, name) -> None:
        self.name=name
        super().__init__()


shop1=shop('apple bd')
shop1.add_product('iphone', 400, 12)
shop1.show_product()

shop1.buy_product('iphone',2)
shop1.show_profit_amount_left()
