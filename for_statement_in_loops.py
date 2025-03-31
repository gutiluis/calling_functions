"""
# for loop loading supplies onto a military truck
# example loading cargo onto a truck
supplies = ["Rations", "Ammo", "Medical Kits", "Water", "Fue"]

for item in supplies:
    print(f"Currently loading: {item} onto the truck.")
print("All supplies loaded. Ready to deploy!")

"""

#soldiers = ["Bernardo", "Brandon", "soldier3", "soldier4", "soldier5", "soldier6", "soldier7", "soldier8", "soldier9", "soldier10"]

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
"""
# countdown from 10 to 1 before an artillery strike is launched
import time
for countdown in range(10, 0, -1):
    print(f"Dropping bombs in: {countdown}")
    time.sleep(1)
print(f"Launcing artillery strike!...")






"""
"""
import time
for i in range(5):
    print(f"{i+1}")
    time.sleep(1)
"""



# distributing ammo to soldiers
#list(zip("abcdefg", range(3), range(4)))
# list of soldiers and list of ammo.
soldiers = ["Delta", "robocop", "z-40"]
#ammo = [30, 40, 50]

#for soldier, rounds in zip(soldiers, ammo):
#    print(f"{soldier} receives {rounds} rounds of ammunition.")


for item in zip([1, 2, 3], ["bomb", "gun", "granade"]):
    print(item)




"""

# fighter jet is on the runway, and takeoff happens in 5 seconds
import time
for countdown in range(5, 0, -1):
    print(f"Takeoff in: {countdown}")
    time.sleep(1)
print(f"The fighter jet is leaving the runway.")
"""
# missile launch authorization, and the system counts from T-minus 20 to liftoff
#for i in range(20, 0, -1):
#    print(f"T-minus {i} for Liftoff.")
#print(f"Missile launch authorized.")






