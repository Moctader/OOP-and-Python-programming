class person:
    id_counter=100
    def __init__(self, email, password) -> None:
        self.email=email
        self.password=password
        # self.user_id=person.id_counter
        # person.id_counter+=1
        self.user_id=person.generate_id()

    @classmethod      #upade generated value inside constructor need classmethod
    def generate_id(self):
        id=self.id_counter
        self.id_counter+=1
        return id
    
    def __repr__(self) -> str:
        return f"email: {self.email} person_id: {self.user_id}"
    

class Product:
    def __init__(self,name, price, quantity) -> None:
        self.name=name
        self.price=price
        self.quantity=quantity
    
    def __repr__(self) -> str:
        return f"product_name: {self.name}|| product_price: {self.price}|| quantity: {self.quantity}"


class Store:
    def __init__(self) -> None:
        self.totall_products={}

    def add_product_store(self, seller_id, product):
        #print(seller_id)
        #print(vars(product))
        productDict=vars(product)
        print(productDict)
        if seller_id not in self.totall_products:
            self.totall_products[seller_id]=[]

            seller_info={}
            seller_info["totall_sell_products"]=0
            seller_info["totall_sell_amount"]=0
            seller_info["totall_profit_amount"]=0
            
            self.totall_products[seller_id].append(seller_info)

        self.totall_products[seller_id].append(productDict)


class Owner(person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        

class sellar(person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)

    def add_product(self,store, product_name, product_price, product_quantity):
        product=Product(product_name, product_price, product_quantity)
        #print(product)
        store.add_product_store(self.user_id, product)



class Customer(person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)

    
    def show_product(self, store):
        #print(store.totall_products)
        all_sellar_keys=store.totall_products.keys()
        #print(all_sellar_keys)
        for sellar_id in all_sellar_keys:
            print("Sellar_id",sellar_id)
            print("================================")
            for index in range(1, len(store.totall_products[sellar_id])):
                #print(product)
                #print("name: ", product["name"], "price:", product["price"], "Quantity:", product["quantity"])

                product=store.totall_products[sellar_id][index]
                print(product["name"],product["price"],product["quantity"])

store=Store()


sellar1=sellar("s",12)
sellar2=sellar("sa",13)
sellar3=sellar("sa",14)
print(sellar1)
print(sellar2)
print(sellar3)

sellar1.add_product(store,'b',133,140)
sellar1.add_product(store, 'a',140,150)

sellar2.add_product(store, 'c',143,140)
sellar2.add_product(store, 'd',163,140)

sellar3.add_product(store, 'e',153,150)
sellar3.add_product(store, 'f',173,190)

#print(store.totall_products)
customer1=Customer("ronok12008@gmail.com", 1234)
customer1.show_product(store)
#print(store.totall_products)
