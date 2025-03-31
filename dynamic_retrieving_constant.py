# interesting descriptors typically run computations instead of returning constants
import os

class DirectorySize:
    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))

class Directory:
    size = DirectorySize() # descriptor instance
    def __init__(self, dirname):
        self.dirname = dirname  # regular instance attribute


a = Directory("songs")
g = Directory("games")
print(a.size)
print(g.size)
#os.remove("games/chess")
#g.size
