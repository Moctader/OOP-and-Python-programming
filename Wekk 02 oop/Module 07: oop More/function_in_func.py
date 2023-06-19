def double_decker():
    print('double decker')
    def fun_inner():
        print('fun inner')
        return 3000
    return fun_inner

print(double_decker()())

# Example 2

def do_something(coding):
    print('work started')
    coding()
    print('work ended')

def coding():
    print('5')

def sleep():
    print('sleeping and dreaming in python')

do_something(coding)
do_something(sleep)