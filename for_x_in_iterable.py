"""
# to check each item
shopping_list = ["Milk", "Eggs", "Bread", "Apples"]

for item in shopping_list:
    print(f"Checking: {item}")


# pour water until bottle is full
# while loop when you don't know exactly how many times to repeat
water_level = 0
bottle_capacity = 5


while water_level < bottle_capacity:
    water_level += 1
    print(f"Filling... {water_level}L")


print("Bottle is full!")


# finding a lost game controller in different locations. stopping once you find it
places = ["office", "gym", "car", "fridge", "backpack"]

for place in places:
    print(f"Looking in {place}...")
    if place == "Drawer":
        print("Found the contoller!")
        break

"""
"""
fuel_level = 0
fuel_tank_capacity = 100

while fuel_level < fuel_tank_capacity:
    fuel_level += 20
    print(f"Refueling... {fuel_level}%")


print("Chopper is fully fueled and ready for takeoff!")
"""

"""
checkpoints = ["Gate A", "Perimeter Fence", "Watchtower", "Main Base"]

for location in checkpoints:
    print(f"Scanning: {location}...")
    if location == "Watchtower":
        print(f"Intruder detected in {location}! Initiating alert!")
        break
"""
"""
# skipping unarmed targets
# target training, skipping unarmed dummies
targets = ["Dummy (unarmed)", "Enemy Soldier", "Enemy Vehicle", "Dummy(unarmed)"]
for target in targets:
    if "unarmed" in target:
        print(f"Skipping {target} (non-hostile)")
        continue
    print(f"Engaging {target}!")
"""
"""
# range in a loop doing military drills
# performing 10 push ups in training
for pushup in range(1, 11):
    print(f"Push-up {pushup}")
print("Training complete!")
"""
# nested loop assigning soldiers to patrol routes
# assigning patrol teams to different locations
soldiers = ["Alpha", "Bravo", "Charlie"]
patrol_routes = ["North Sector", "South Sector", "East Sector"]

for soldier in soldiers:
    print(f"{soldier} team assigned to:")
    for route in patrol_routes:
        print(f" - {route}")

