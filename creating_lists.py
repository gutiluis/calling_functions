def get_list():
    get_list.n = [] # property of the function object. not a local variable


get_list()
print(get_list.n)
# unconventional
class Acc:
    def get_list():
        get_list.a = []

# conventional
class Acc:
    @staticmethod
    def get_list():
        Acc.get_list.a = []

Acc.get_list()
print(Acc.get_list.a)

class Acc:
    def __init__(self):
        self.a = []
acc1 = Acc()
print(acc1.a)



"""
print(type([]))
print(id([]))
# print(hash([])) # unhashable
a = []
v = ["concatenate"]
print(a.__add__(v)) # can use in a method of a class
print(a.__class__())


print([] + ["sec"] + ["third"])

print(dir([]))

"""
