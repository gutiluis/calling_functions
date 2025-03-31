import os

class Print_ls_man:
    def __get__(self, obj, objtype=None):
        return (os.system(obj.man))

class Mine:
    descriptor_instance = Print_ls_man()
    def __init__(self, man):
        self.man = man


a = Mine("man ls")
a.descriptor_instance
