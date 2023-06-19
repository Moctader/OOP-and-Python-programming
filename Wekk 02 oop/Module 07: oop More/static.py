class shopping:
    cart=[]
    origin='china'

    def __init__(self, name, location) -> None:
        self.name=name
        self.location=location
    
    @staticmethod
    def multiply(a, b):
        
        print(a*b)


shopping.multiply(3,4)