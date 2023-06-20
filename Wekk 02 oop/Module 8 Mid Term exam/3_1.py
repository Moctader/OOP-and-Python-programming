class operation:
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c

    def sum(self):
        return self.a+self.b+self.c
    
    
    def factorial(self):
        fact=1
        for num in range(1, self.b+1):
            fact*=num
        return fact
    

method=operation(2,3,4)
print(method.sum())

print(method.factorial())
