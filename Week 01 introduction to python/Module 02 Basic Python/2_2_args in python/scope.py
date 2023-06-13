balance=3000

def value(item, price):
    global balance
    print(f'balance befor buy', balance)
    balance=balance-price
    print(f'balance after buying {item} is: ', balance)

value('sunglass', 1000)