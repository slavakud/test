from time import sleep
from functools import wraps
def wait (*n):
    def func(func_1):
        def print_text(*args,**kwargs):
            print("start sleep function summ")
            func_1(*args,**kwargs)
            sleep(n[0])
            print (f"There was a pause {n} seconds before execution {func_1.__name__ }")
        return print_text
    return func

# return func


@wait(7)
def summ(*args,**kwargs):
    sum=0
    for number in range(1,len(args)):
        sum +=args[number]
    print(sum)


summ(2,4,5,6,7,8,9)
