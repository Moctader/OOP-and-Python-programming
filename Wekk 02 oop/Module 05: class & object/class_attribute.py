class shop:

    cart=[]
    def __init__ (self, buyer):
        self.buyer=buyer

    def add_to_cart(self, item):
        self.cart.append(item)
    

d=shop('v')
d.add_to_cart('nothing')
print(d.cart)

l=shop('uuu')
l.add_to_cart('everything')
print(l.cart)
