import math
import time

def timer(fun):
    def inner_fun(*args, **kwargs):
        start=time.time()
        fun(*args, **kwargs)
        end=time.time()
        print(f'totall time taken{end-start}')
    return inner_fun

@timer
def get_factorial(n):
    result=math.factorial(n)
    print(f'factoral of {n} is {result}')
    print('nothing is impossible')

get_factorial(n=1200)