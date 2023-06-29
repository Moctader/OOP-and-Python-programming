class person:
    int_count=0
    def __init__(self, email, password) -> None:
        self.email=email
        self.password=password
        self.user_id=person.generating_id()

    @classmethod
    def generating_id(self):
        id=self.int_count
        self.int_count+=1
        return id

    def __repr__(self) -> str:
        return f"email: {self.email}, password: {self.password}"
        
class Product:
    def __init__(self, name, price, quantity) -> None:
        self.name=name
        self.price=price
        self.quantity=quantity

    def __repr__(self) -> str:
        return f" name: {self.name} price: {self.price} quantity:{self.quantity}"
    
class Store:
    def __init__(self) -> None:
        self.totall_products={}

    def add_product_to_store(self, seller_id, product):
        print(vars(product))
        print(seller_id)



class Owner(person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)

class Seller(person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)

    def add_product(self, name, price, quantity):
        product=Product(name, price, quantity)
        Store1.add_product_to_store(self.user_id, product)


class customer(person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)

    def show_products(self, store1):
        all_the_keys=Store1.totall_products.keys()
        for sellar_id in all_the_keys:
            print(sellar_id)
            print("================================")
            for index in range(1, len(store1.totall_products[sellar_id])):
                product=store1.totall_products[sellar_id][index]
                print(product["name"], product["price"], product["quantity"])




Store1=Store()
Seller1=Seller("gmail", 1234)
Seller2=Seller("gmail", 1234)
Seller3=Seller("gmail", 1234)

Seller1.add_product("dkfdsks", 34, 56)
Seller1.add_product("dkfdsks", 34, 56)

Seller2.add_product("dkfdsks", 34, 56)
Seller2.add_product("dkfdsks", 34, 56)

Seller3.add_product("dkfdsks", 34, 56)
Seller3.add_product("dkfdsks", 34, 56)
