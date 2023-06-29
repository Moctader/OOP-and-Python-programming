class Customer:
    def __init__(self, email, password) -> None:
        self.email=email
        self.password=password
    
    def creat_account(self):
        print("You account has succesfully created")
        

class App_function:
    def __init__(self) -> None:
        self.customers=[]
        
    def register(self):
        email=input("please enter your email: ")
        password=input("please enter your passwprd: ")
        customer=Customer(email, password)
        self.customers.append(customer)
        customer.creat_account()
        print("Your account successfully created")
    
    def login(self):
        email=input("Enter your email: ")
        password=input("Enter your password: ")
        
        for customer in self.customers:
            if customer.email==email and customer.password==password:
                print("Login Successful")
                return
            else:
                print("Invalid email or password")

App=App_function()
print("1 register")
print("2 login")
choice=input("Enter your choice: ")

if  choice=="1":
    App.register()
elif choice=="2":
    App.login()
else:
    print("invalid choice")
        
    
        