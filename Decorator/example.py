def check_for_positive(n):
    return True if n>=0 else False

def check_for_positive_decorator(fun):
    def wrap(*args, **wargs):
        if check_for_positive(*args):
            return fun(*args, *wargs)
        else:
            return "Number is negative"
    return wrap

@check_for_positive_decorator
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(-1))
print(factorial(4))

