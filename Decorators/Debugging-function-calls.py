
def debug(func):
    def wrapper(*args,**kwargs):
        result =func(*args,**kwargs)
        # to create the string of all the args 
        # this is comprehension loop
        args_values=','.join(str(arg) for arg in args) 
        kwargs_values=','.join (f"{k}={v}" for k,v in kwargs.items())
                                

        print (f" calling : {func.__name__} \n args: {args_values} \n kwargs: {kwargs_values}")
        return result

    return wrapper #  this returns the definition of wrapper function to the decorator 




@debug
def greet(name, greeting="Hello",**kwargs):
    print (f"{greeting},{name}")
    for k,v in kwargs.items():
        print (f"{k}: {v}")


greet("Areeba","HI",age=12,city="london")


