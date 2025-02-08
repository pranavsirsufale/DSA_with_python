#

#//? Debugging Function Caslls

#//! Create a decorator to print the function name and the values of its arguents every time the function is called.


def debug(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper

@debug
def greet(name, greet):
    print(f'{greet} , {name}')


greet('pranav' ,'hellow')











