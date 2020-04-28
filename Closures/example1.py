#---- Local variable concept
def fun():
    x = 3
    def fun2():
        x = 4
        print(x)
    fun2()
    print(x)

fun()

# o/p 4  3
# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6
# Nonlocal variable

def funx():
    x = 3
    def fun1():
        nonlocal x
        x = 4
        print(x)
    fun1()
    print(x)
funx() # o/p   4   4


# global variable

y = 6
def fun_y():
    print(y)  #6
    def fun_y1():
        y = 12
        print(y)  # 12
    fun_y1()
    print(y) # 6
fun_y()


#Make same global variable accessible to inner function

z = 3
def fun_z():
    print(z)  # 3
    def fun_z1():
        global z
        z = 32
        print(z) # 32
    fun_z1()
    print(z) #32
fun_z()


