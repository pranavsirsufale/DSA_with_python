#

#//? Debugging Function Caslls

#//! Create a decorator to print the function name and the values of its arguents every time the function is called.

'''
def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f'{k}={v}' for k,v in kwargs.items())
        print(f'calling : {func.__name__} with args {args_value} and kwargs {kwargs_value}')
        return func(*args,**kwargs)
    return wrapper

@debug
def greet(name, greet):
    print(f'{greet} , {name}')


greet('pranav' ,'hellow')
'''

#??? chache Return Value
#! Implement a decorator that caches the return values of a function, so that when it's called with the same arguments , the cached value is returned instead of re-executing the function

import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a + b 

print(long_running_function(2,3))
print(long_running_function(2,3))