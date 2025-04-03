def x():
    a = input("Enter a weapon: ")
    while True:
        if not a is True: # empty string is bool false. no input in a variable
            raise Exception("Enter a value")
        elif a == "gun":
            print("Kill with a gun.")
            break
        elif a == "bazooka":
            print("Kill with a bazooka")
            break


x()

