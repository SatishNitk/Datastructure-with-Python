def fab():
    a = 0
    b = 1
    while True:
        c = a +b
        yield c
        a = b
        b = c
f = fab()
for _ in range(10):
    print(next(f))