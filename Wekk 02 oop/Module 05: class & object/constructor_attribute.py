class shop:

    def __init__(self, buyer):
        self.buyer=buyer
        self.cart=[]

    def add_to_cart(self, item):
        self.cart.append(item)



zk=shop('tt')
zk.add_to_cart('shoes')
zk.add_to_cart('mouse')
print(zk.cart)

zm=shop(' a')
zm.add_to_cart(1900)
print(zm.cart)