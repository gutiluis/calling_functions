def n():
    bullets = 100
    attack = 20
    while bullets > 1:
        print("Start attack with", bullets, "bullets")
        print("Bullets needed for attack:", attack)
        bullets -= attack
        print("Remaining bullets after attack.", bullets)
n()


print("="*30)
def fuel_for_strike():
    fuel = 100
    while fuel > 1:
        print("Enough fuel for attack:", fuel)
        c = input("First attack?")
        fuel -= 50
        print("Remaining fuel before refueling:", fuel)
        c = input("Second attack?")
        fuel -= 50
        print("Remaining fuel before refueling:", fuel)
        k = input("Must refuel...")
        fuel += 100
        print("Current level:", fuel)
fuel_for_strike()

print("="*30)
targets = 0
while targets == 0:
    print("There is no attack")
    break
    if targets == 1:
        print("Destroy targets")
print("End loop")

print("===============================")
count = 0
while count < 5:
    print("count is:", count)
    count += 1


print("===============================")
count_weapons = 1
count_target = 1
while count_weapons < 3 and count_target < 3:
    print("The weapon count is", count_weapons, count_target)
    count_weapons += 1
    count_target += 1

print("===============================")
# how many elements in list
numbers = [1, 3, 5, 2, 7, 4, 2]
i = 0
count_numbers = 0
while i < len(numbers):
    if numbers[i] == 2:
        count_numbers += 1
    i += 1
print(count)
