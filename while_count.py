def n():
    target = input("Enter the target: ")
    attempt_count = 1
    while target != "vancouver":
        if attempt_count > 3:
            print("Too many attempts:")
            break
        target = input("Invalid target. Do not attack until location is granted ")
        attempt_count += 1
    print("Destroying location.")

n()

