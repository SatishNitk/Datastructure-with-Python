#https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6
"""   

To define a closure we need an inner function that:
1-It should be returned by the outer function.
2- it should capture some of the nonlocal variables of the outer function.
         This can be done by accessing those variables, 
   or    defining them as a nonlocal variable
   or    having a nested closure that needs to capture them.

"""


#inner funciton
def fun():
    x = 8

    def fun1():
        y = 7
        print(y) # 7
        print(x) # 8
    fun1()
fun()


# closure Ex-1

# __code__.co_freevars this return the set of variable that is used by inner function from enclsong funtion, if it not using any variable of enclosing function means
# that is not a closure. To be a closure it should acces atleast one of the paren function variavle



def fun_x():
    x = 3
    def fun_y():
        y = x + 1
        print(y) # 4
    print(x) # 3
    return fun_y
var = fun_x()
var()
print(var.__code__.co_freevars) # o/p : - ('x',)

# closure EX - 2

def fun_y():
    y = 3
    def fun_y():
        nonlocal y  # i am not using y but it should be available in function fun_y context thats why its a closure
        print("satish")
    print(y)
    return fun_y
v = fun_y()
v()
print(v.__code__.co_freevars)  # o/p :- ('y',)






#Its not a closure because it is not using any enclosing function variable

def fun_z():
    x = 32
    def fun_z1():
        print("satish")
    print(x)
    return fun_z1
t = fun_z()
t()
print(t.__code__.co_freevars)  # o/p :- () :- empty set




# nested closure

def f(x):
    def g(y):
        def h(z):
            return x * y * z
        print(y)
        return h
    return g
a = 5
b = 2
c = 1
f(a)(b)(c)  # Output is 10
print(f(a)(b).__code__.co_freevars)  # o/p :- ('x', 'y') 


# Decorator Example:

def deco(f):
    def g(*args, **kwargs):
        return f(*args, **kwargs)  # line 95 and 96 are closure
    return g
def func12(x):
     return 2*x
func1 = deco(func12)
print(func1(2))  # Output is 4





