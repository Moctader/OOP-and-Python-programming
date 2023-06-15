
value=lambda x:x*2
x=value(44)
print(x)

# add=lambda x, y: x+y
# v=add(3,4)
# print(v)

numbers=[12, 35, 68, 45, 89]
double_nums=map(value, numbers)
squred__nums=map(lambda x: x**2, numbers)
print(list(double_nums))
print(list(squred__nums))

actors=[{'name':'ali', 'age':65},
    {'name':'aliii', 'age':5},
    {'name':'alsssi', 'age':45},
    {'name':'aldcdci', 'age':65},
    {'name':'aaa', 'age':50},
    {'name':'alcdcaci', 'age':25}
    ]

juniors=filter(lambda actor:actor['age']<40, actors)
print(list(juniors))
juni_y=filter(lambda actor : actor['age']%5==0, actors)
print(list(juni_y))

# numbers = [9, 15, 2, 36]
# numbers[1:4] = [20, 14, 36]
# print(numbers)
