"""
# for loop loading supplies onto a military truck
# example loading cargo onto a truck
supplies = ["Rations", "Ammo", "Medical Kits", "Water", "Fue"]

for item in supplies:
    print(f"Currently loading: {item} onto the truck.")
print("All supplies loaded. Ready to deploy!")

"""

soldiers = ["Bernardo", "Brandon", "soldier3", "soldier4", "soldier5", "soldier6", "soldier7", "soldier8", "soldier9", "soldier10"]

#for soldier in soldiers:
#    print(f"The soldier {soldier} is assigned to a mission.")
#print("All the soldiers have been assigned to a mission.")


"""
weapons = ["gun", "bazooka", "granade"]
for weapon in weapons:
    print(f"Checking {weapon} before deployment",
    f"Inspecting the {weapon} before battle.", sep="...")
print()
print("Inspection complete. Get ready for battle.")
"""
"""
# counting down for paratroopers jump
# write a countdown starting from 5 before soldiers jump out of an aircraft
jump = 0
starting_countdown = 6

while starting_countdown > jump:
    starting_countdown -= 1
    print(f"Paratroopers jump in: {starting_countdown} seconds")


print("Jump!")
"""
"""
for countdown in range(5, 0, -1):
    print(f"Paratroopers jump in: {countdown} seconds!")
print("Jump!")
"""

ammo = ["gun", "bazooka", "granade", "bomb"]
