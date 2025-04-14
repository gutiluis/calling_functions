#
class X:
    def __init__(self):
        self.name = []

#
class Y:
    def __init__(self, weapon):
        self.weapon = weapon

#
class A:
    def __init__(self):
       pass
    def attack(self, target):
        return f"{target}"



a = X()

b = Y("Gun")
print(b.weapon)

c = A()
print(c.attack("vancouver"))
