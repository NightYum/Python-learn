from typing import Callable
import time

def decorator(func: Callable):
    def wrapper():
        print(func.__name__)
        res = func()
        return res
    return wrapper

@decorator
def decorated():
    return 1

# new_func = decorator(my_func)
# print(new_func)



def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f'Исполнения заняло {end - start}')
        return res
    return wrapper

@timer
def big_for(n: int = 0) -> int:
    for i in range(100):
        for j in range(1000):
            for k in range(1000):
                n += 1
    return n

# new_func = timer(big_for)(3)
# print(new_func)
#
# print(big_for(n = 10))

def limit_calls(limit: int, func: Callable):
    def wrapper(func: Callable):
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            return res
        return inner
    return wrapper

@limit_calls(limit=3)
def my_func(n: int = 0):
    for i in range(100):
        for j in range(1000):
            n += 1
    return n

print(my_func())