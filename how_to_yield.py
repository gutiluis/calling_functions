a = list(input("Enter something: "))

def to_yield(data):
    for k in data:
        yield k


o = to_yield(a)
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
