import time


def time_result(fun):
    def timer(*args,**kwargs):
        start_time = time.time()
        fun()
        end_time = time.time()
        print(end_time-start_time)
        return fun
    return timer


@time_result
def result():
    print(sum(number for number in range(10000000)))
result()