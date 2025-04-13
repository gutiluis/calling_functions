import datetime


weapon = input("Enter weapon: ")
target = input("Enter target: ")




class Drone:
    def __init__(self, weapon, target):
        self.weapon = weapon
        self.target = target
        self.ddt = datetime.datetime.now()
    def set_attack(self):
        return f"The attack will be the {self.ddt.strftime("%d-%m-%Y")} with a {self.weapon} and on {self.target}"


n = Drone(weapon, target)
print(n.set_attack())


#        input
 #       instance attribute parameter def __init__(self, c):
  #      method attribute parameter def a(self, s):
