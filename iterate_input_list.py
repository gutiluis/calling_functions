def x():
    wea = input(["Enter weapons: "]).split()
    for temp_var in wea:
        print(temp_var)
    print(temp_var) # prints last iteration

    print("Weapons: ")
    for i in wea:
        print("* " + i) # unicode

    print("#"*20)

    def hasher():
        for i in wea:
            print(hash(i))
        for i in wea:
            print(i, hash(i))

    hasher()
    print("#" * 20)
    
    def index():
        return wea[0] in wea # if the list has more items add more slices

    print(index())
    print("#" * 20)

    def all_function():
        return all(wea) # bool
    print(all_function())


def c():
    continents = [
        "Asia",
        "South America",
        "Noth America",
        "Africa",
        "Europe",
        "Antartica",
        "Australia",
    ]
    for i in continents:
        print("*", i)



if __name__=="__main__":
  #
  #   x()
    c()