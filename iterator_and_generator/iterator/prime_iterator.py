import math
class Prime:

    def __init__(self):
        self.first_prime  = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.first_prime += 1
        print("number", self.first_prime, end = "")
        if self.first_prime == 2:
            return True
        else:
            for i in range(2, int(math.sqrt(self.first_prime)) + 1):
                if self.first_prime % i == 0:
                    return False
            return True
p = Prime()
prime = iter(p)
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))

