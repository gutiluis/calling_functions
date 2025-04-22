def write():
    with open("test.txt", "w") as f:
        def x():
            appender = []
            while True:
                wea = input("Enter weapons: ")
                if wea == "exit":
                    break
                elif len(wea) >= 1:
                    print("Using: {}".format(wea))
                    appender.append(wea)
                elif not wea:
                    break       
            print("Using {}".format(appender))
            f.write("\n".join(appender)) # save to file
        x()
    f.close()


def k():
    tar = [
        "vancouver",
        "richmond", #always use comma at the last element in a list value last index
    ]
    print(f"These are the selected targets: {tar}")
    if tar[0]:
        print("Attack {}.".format(tar[0]))
        if tar[1]:
            print("Try {} after.".format(tar[1]))
    def forg():
        prompt = "Want to extend the list? "
        extend_targets = input(prompt)
        if extend_targets == "no":
            pass
        else:
            tar.extend("Calgary")
            print(tar)
        return
    forg()

def emoji():
    lunch = "\N{TACO}"
    print("Now you can have: \n{}.".format(lunch))
    mon = "\N{MONKEY}"
    print("{}.".format(mon))

def time_of_attack():
    import datetime
    c = datetime.datetime.now()
    print(c)



if __name__=="__main__":
    write()
    k()
    emoji()
    time_of_attack()
