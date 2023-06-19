"""
Create a Product class and a Shop class.
Inside the Shop class, create a method name add_product which adds products using the 
Product class to the Shop class.Inside the Shop class, create a method name buy_product
 which is used to buy a product and check whether this product is available or not. 
 If you successfully buy a product, then throw a Congress message.

"""


class Product:
    def __init__(self, name, price, quantity) -> None:
        self.product_name=name
        self.product_price=price
        self.product_quantity=quantity


class store:
    def __init__(self) -> None:
        self.__product_price={}
        self.__product_quantity={}
        self.__product_profit=0
    

    def add_product(self, name, price, quantity):
        product=Product(name, price, quantity)
        self.__product_price[product.product_name]=product.product_price
        self.__product_quantity[product.product_name]=product.product_quantity


    def buy_product(self, name, quantity):
        if name in self.__product_price:
            if self.__product_quantity[name]>=quantity:
                self.__product_quantity[name]=self.__product_quantity[name]-quantity
                #profit calculation 5%
                self.__product_profit+=((5*self.__product_price[name])/100)*quantity
                print('Thank you')
            else:
                print('unavailable')
        else:
            print('Not found')

    def show_product(self):
        print(f'product price {self.__product_price}')
        print(f'product Quantity {self.__product_quantity}')
    
    def show_profit(self):
        print('profit', self.__product_profit)



class shop(store):
    def __init__(self, name) -> None:
        self.name=name
        super().__init__()


shop1=shop('values')
shop1.add_product('iphone', 400, 12)
shop1.buy_product('iphone', 2)
shop1.show_product()
shop1.show_profit()
shop1.show_product()
