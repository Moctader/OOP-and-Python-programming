class shop:

    def __init__(self, name):
        self.name=name
        self.cart=[]
    
    def add_to_cart(self, item, price, quantity):
        product={'item':item, 'price':price, 'quantity':quantity}
        self.cart.append(product)
    
    def checkout(self, amount):
        total=0
        for item in self.cart:
            total+=item['price']*item['quantity']
        
        if amount>total:
            print(f'please return money: {amount-total}')
        elif amount<total:
            print(f'please add money: {total-amount}')
    

buyer=shop('something')
buyer.add_to_cart('alu', 50, 6)
buyer.add_to_cart('rice', 50, 5)
buyer.add_to_cart('dim', 12, 24)
buyer.checkout(int(input()))