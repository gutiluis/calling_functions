def n():
    gas_fuel = 0
    targets = []
    has_weapon = True
    while gas_fuel < has_weapon:
        print(f"Start attack with {gas_fuel} gas fuel")
        targets.append(gas_fuel)
        gas_fuel = gas_fuel + 1
        print("Gas needed for attack: ", targets)
        print(f"Gas for next target {gas_fuel}")
    print("Gas used in targets: ")
    for target in targets:
        print(targets)

n()
