class claculator:
    brand='casio 990'

    def add(self, num1, num2):
        value=num1+num2
        return value
    
    # deducte method

    def deduct_method(self, num1, num2):
        value=num1-num2
        return value
    
    #multiply method

    def multiply_method(self, num1, num2):
        value=num1*num2
        return value
    
    #divided method

    def divided_method(self, num1, num2):
        value=num1//num2
        return value
    

my_calculator=claculator()
result_add=my_calculator.add(1,2)
print(result_add)

result_deduct=my_calculator.deduct_method(4,2)
print(result_deduct)

result_multiply=my_calculator.multiply_method(2,2)
print(result_multiply)

result_divided=my_calculator.divided_method(6, 2)
print(result_divided)