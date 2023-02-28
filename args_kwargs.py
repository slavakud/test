def args(function):
    def print_args_kwargs(*args,**kwargs):
        print(*args,**kwargs)
        result = function(*args,**kwargs)

        return print_args_kwargs
    return print_args_kwargs


@args
def values(number,list):
    print(number+list)
x=values(2,5)
