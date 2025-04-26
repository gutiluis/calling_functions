weapons = [
    "gun",
    "bazooka",
    "granade",
    ]
targets = [
     "Vancouver",
     "Germany",
     "Russia",
]
    
def display_missions(display_name, missions):
    print(display_name + ":")
    suggested_mission = missions.pop(0) # how to use random?
    print("======>", suggested_mission, "<=========")    
    for i in missions:
        print("* " + i)
    print()


display_missions("Weapons", weapons)
display_missions("Targets", targets)

def display_targets(display_name, targ):
    import random
    print(display_name + ":")
    f = random.choice(list(targets))
    print("====>", f, "<====")
    for i in targ:
        print("* " + i)
    print()
    
display_targets("Targets", targets)
