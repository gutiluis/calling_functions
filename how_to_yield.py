a = list("enter")

def to_yield(a):
    for k in a:
        for line in k:
            yield line


o = to_yield(a)
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))



