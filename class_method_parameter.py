class Drone:
    def __init__(self, target):
        self.target = target
    def return_weapon_and_target(self, weapon): # extra parameter
        return f"The Drone will kill you with a: {weapon}, on {self.target}"


a = Drone("Vancouver")
print(a.return_weapon_and_target("Missile"))
