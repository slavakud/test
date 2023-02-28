from functools import wraps
def decorator(function):
    @wraps(function)
    def print_Hello_decoration(*args,**kwargs):
        print (f" Hello decoration {function(*args,**kwargs)}")
    return print_Hello_decoration

@decorator
def su(x,y):
    return x+y
su(4,3)

@decorator
def name(x):
    return x
name(" Jack")
x= su(4,15)
print(x)