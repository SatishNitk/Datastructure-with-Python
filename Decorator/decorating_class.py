
def check_positive(func):
    def func_wrapper(*args):
        for arg in args:
            if type(arg) is int or type(arg) is float:
                if arg < 0:
                    raise Exception("Method {} takes only positive arguments".format(func.__name__))
        return func(*args)

    return func_wrapper
    
class Operations:
    @check_positive
    def average(self, x, y):
        return (x + y)/2


op = Operations()
print(op.average(23,4))