# def famous_name(name1, n2, **kargs):
#     name=f'{name1} {n2}'

#     #print(kargs['fourth'])
#     for key, value in kargs.items():
#         print(key, value)
#     return name

# names=famous_name(n2='j',name1='e', third='names', fourth='anything')
# print(names)

def famous_name(n1, n2, **kargs):
    name=f'{n1} {n2}'
    #print(kargs)
    for key, value in kargs.items():
        print(key,': ', value)
    return name

name=famous_name(n1='l',n2='h', n3='r',n4='o', n5='w')
print(name)


#return multiple things from an array
def a_lot_num(num1, num2):
    mult=num1*num2
    add=num1+num2
    divi=num1-num2
    return [mult, add, divi]

everythin=a_lot_num(2, 4)
print(everythin)
