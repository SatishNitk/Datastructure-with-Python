
class MyDecorator: 
    def __init__(self, function): 
        self.function = function 
    
    def __call__(self): 
        self.function() 


# adding class decorator to the function 
@MyDecorator
def function(): 
    print("GeeksforGeeks") 
function()
              #   OR
fun_object = MyDecorator(function)  # init will executed from here
fun_object()                        # call will be executed from here



print("\n\n EX-2 O/P \n\n")

# EX-2

# Python program showing 
# class decorator with 
# return satement 

class SquareDecorator: 

    def __init__(self, function): 
        self.function = function 

    def __call__(self, *args, **kwargs): 
        result = self.function(*args, **kwargs) 
        return result 

@SquareDecorator
def get_square(n): 
    print("given number is:", n) 
    return n * n 

print("Square of number is:", get_square(195)) 


