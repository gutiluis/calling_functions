import datetime


class Drone:
    def __init__(self, weapon, target):
        self.ddt = self.time_attack()
        self.weapon = weapon
        self.target = target
    def time_attack(self):
        self.ddt = datetime.datetime.now()
        return self.ddt.strftime("%m-%d-%Y")
    def return_attack(self):
        return f"Destroying the: {self.time_attack()}, Using: {self.weapon}, The city of: {self.target}"


f_drone = Drone("Missiles", "Vancouver")
print(f_drone.return_attack())
