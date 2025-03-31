import os

class Print_current_d(object):
    def __get__(self, obj, objtype=None):
        return (os.listdir())

class Listdir:
    des_ins = Print_current_d() # descriptor instance
    def __init__(self):
        return


inst = Listdir()
print(inst.des_ins) # descriptor lookup
