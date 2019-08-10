# Decorators are high order function which takes a func as arg and add functionality to it
# and returns the function whithout altering the source code of the passed in function.

import time

def timeit(func):
    # returns an inner function ready to be executed.
    def wrapper(*args, **kwargs):
        start = time.time()
	#func is waiting to be executed
        func
        end = time.time()
        print('Total time of execution:: ' + str(end - start))
    return wrapper


@timeit
def speed_list():
    for i in range(10000):
        empty_list.append(i**2)
    print(empty_list)


@timeit
def speed_lc():
    empty_list = [i**2 for i in range(10000)]
    print(empty_list)


l1 = speed_list()
lc2 = speed_lc()

