print("EXample -1 o/p")

# EX- 1
def time_this(original_function):      
    def new_function(*args,**kwargs):
        import datetime 
        print("inner function start", args)
        before = datetime.datetime.now()                     
        x = original_function(*args,**kwargs)                
        after = datetime.datetime.now()                      
        print("Elapsed Time = {0}".format(after-before))
        return x                                             
    return new_function                                   
    
@time_this
def func_a(stuff):
    import time
    time.sleep(3)
    print("in last")
    return "satish"

k = func_a(1)
print(k)

print("\n\n\n")

#EX-2
print("\n EXample -2 o/p\n")

import datetime
def time_this1(original_function1):                           
    def new_function(*args,**kwargs):                        
        before = datetime.datetime.now()                     
        x = original_function1(*args,**kwargs)                
        after = datetime.datetime.now()                      
        print("Elapsed Time = {0}".format(after-before))
        return x                                             
    return new_function 


def do_important_things_1():
    print("Import something ")


def do_important_things_2():
    print("Import something ")


def do_important_things_3():
    print("Import something")


def func_a():
    do_important_things_1()
    do_important_things_2()
    do_important_things_3()

func_a1 = time_this1(func_a) 
func_a1()

print("\n\n\n")

# EX- 3
print("EXample -3 o/p \n")

def do_something(*args, **kwargs):
    print("sart of extra work", args, *kwargs)
    
    
def outer_decorator(*outer_args,**outer_kwargs):                            
    def decorator(fn):                                            
        def decorated(*args,**kwargs):                            
            do_something(*outer_args,**outer_kwargs)                      
            return fn(*args,**kwargs)                         
        return decorated                                          
    return decorator       
    
@outer_decorator(1,2,3)
def foo(a,b,c):
    print(a)
    print(b)
    print(c)


foo(4,5,6)

