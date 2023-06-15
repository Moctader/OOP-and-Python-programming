
def fib(value):
    if value is 0:
        return 0
    if value<=1:
        return 1
    # if value>=1 and value<=2:
    #     return 1
    else:

        return (fib(value-1)+fib(value-2))

value=int(input())

if value <= 0:  
   print("Plese enter a positive integer")  
else:  
    for i in range(value):
        print(fib(i))

#Not working properly