def x():
    appender = []
    while True:
        wea = input("Enter weapons: ")
        if len(wea) >= 1:
            print("Using: {}".format(wea))
        elif len(wea) < 1:
            break
        appender.append(wea)    

def k():
    tar = [
        "vancouver",
        "richmond", #always use comma at the last element in a list value last index
    ]
    if tar[0]:
        print("Attack {}.".format(tar[0]))
        if tar[1]:
            print("Try {} after.".format(tar[1]))

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
    x()
    k()
    emoji()
    time_of_attack()