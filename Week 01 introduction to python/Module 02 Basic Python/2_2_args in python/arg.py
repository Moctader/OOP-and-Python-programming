def numbers(val, *args):
    print(args)
    sum=0
    for num in args:
        #print(num)
        sum=sum+num
    return sum



totall_sum=numbers(2,2, 4)
print('totall sum: ',totall_sum)