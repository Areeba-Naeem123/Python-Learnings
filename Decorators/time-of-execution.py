import time

# most commonly when we make decorators we need to make nested functions 

def timer(func):
    def wrapper (*args,**kwargs):
        start=time.time()

        result=func(*args,**kwargs)
        end=time.time()
        print (f"{func.__name__} ran in {(end-start)}")
        return result
    return wrapper # this returns to the decorator


@timer # here this decorator restricts the function to always pass through timer function first then execute


def example_function(n):
    time.sleep(n)


example_function(2)
