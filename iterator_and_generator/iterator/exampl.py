class Iterator(object):

    def __init__(self, name, counter):
        print("from __init__")
        self.name = name
        self.counter = counter

    def __iter__(self):
        print("from __iter__")
        self.count = 0
        return self

    def __next__(self):
        print("from __next__")
        if self.count < self.counter:
            self.count += 1
            return self.name
        else:
            raise StopIteration

it_obj = Iterator("satish", 3)  # init called here
for it in it_obj: # iter than next called here
    print(it)
print("\n\n\n\n")

it_obj = Iterator("satish", 3)  # init called here
it = iter(it_obj)  # iter called here
print(next(it))   # next called heer
print(next(it))
print(next(it))
print(next(it))

