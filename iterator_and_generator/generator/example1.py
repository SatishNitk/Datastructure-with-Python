import math
def prime():
    n = 2
    while True:
        flag = False
        if n ==2:
            yield True
        else:
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    flag = True
                    yield False
                    break
            if not flag:
                yield True
        n = n + 1
p = prime()
for i in range(15):
    print(next(p))