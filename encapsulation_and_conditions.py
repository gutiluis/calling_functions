class Drone:
    def __init__(self, weapon, target):
        self.weapon = weapon
        self.__target = target
    def display(self):
        return f"{self.weapon} destroy {self.__target}"
    def set_target(self, target):
        if target != self.target:
            self.__target = target
        else:
            print("invalid target")

a = Drone("a", "b")
a.display()
a.set_target("c")
a.display()
