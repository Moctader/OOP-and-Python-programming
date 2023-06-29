class person:
    id_counter=100
    def __init__(self,email, password) -> None:
        self.email=email
        self.password=password
        self.user_id=person.generating_id()

    @classmethod
    def generating_id(self):
        id=self.id_counter
        self.id_counter+=1
        return id
        
    def __repr__(self) -> str:
        return f"email: {self.email}, password:{self.password}"

class Product:
    def __init__(self, name, price, quantitiy) -> None:
        self.name=name
        self.price=price
        self.quantity=quantitiy

    def __repr__(self):
        return f"product_name: {self.name}||  product_price: {self.price}||  product_quantity: {self.quantity}"

class Store:
    def __init__(self) -> None:
        self.totall_products={}

    def product_add_to_store(self, seller_id, product):
        productDict=vars(product)

        if seller_id not in self.totall_products:
            self.totall_products[seller_id]=[]
            seller_info={}
            seller_info["Totall_sell_products"]=0
            seller_info["Totall_sell_amount"]=0
            seller_info["Totall_amount_profit"]=0
        self.totall_products[seller_id].append(productDict)

 
   
class Owner(person):
    pass

class Seller(person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)

    def add_product(self, product_name, product_price, product_quantity):
        product=Product(product_name,product_price, product_quantity)
        store.product_add_to_store(self.user_id,product)
        

class Customer(person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)

    def show_products(self, store):
        #print(store.totall_products[100])
        all_selars_key=store.totall_products.keys()
        for sellar_id in all_selars_key:
            print("sellar_id", sellar_id)
            print("==================================")
            for index in range(1, len(store.totall_products[sellar_id])):
                product=store.totall_products[sellar_id][index]
                print(product["name"], product["price"], product["quantity"])





store=Store()

Seller1=Seller("s", 12)
Seller2=Seller("sa", 122)

print(Seller1)


Seller1.add_product("sa", 122,140)
Seller1.add_product("saaa", 125,1455)

Seller2.add_product("saaa", 125,1455)
Seller2.add_product( "saaa", 125,1455)
#print(store.totall_products)
customer1=Customer("ronok12008@gmail.com", 1234)
customer1.show_products(store)
