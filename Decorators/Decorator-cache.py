
import time 


def cache(func):
    cache_value={}
    print (cache_value)
    def wrapper (*args,**kwargs):
        if args in cache_value:
            return cache_value[args]
        result= func(*args)
        cache_value[args]=result
        return result
    
        
    return wrapper



@cache
def long_running_func(a,b):
    print("before sleep")
    time.sleep(4)
    print("after sleep")

    return a+b

print (long_running_func(2,3))
print (long_running_func(2,3)) # this function will not execute again bcz its result is already stored 
print (long_running_func(7,3))



