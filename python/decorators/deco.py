# learn about decorators 
#? Timiing function Execution
#//! Write a decorator that measures the time a function takes to execute 


#? Debugging Function Calls 
#??! Create a decorator to print the function name and the values of its arguments every time the function is called 


import time 

def timer(func):
    def wrapper(*args,**kwars):
        start = time.time()
        result = func(*args, **kwars)
        end = time.time()

        print(f'{func.__name__} ran in {end-start} time')
        return result

    return wrapper


@timer
def example_function(n):
    time.sleep(n)


# print(example_function(2))
