user = input("User name: ")
prompt = "> "

print(f"Hi {user}")

def n():
    v = []
    while True:
        w = print(f"Select Weapons: ")
        weapons = input(prompt)
        if weapons == "exit":
            break
        v.append(weapons)
    return v

def t():
    k = []
    while True:
        i = print(f"Select Targets: ")
        targets = input(prompt)
        if targets == "exit":
            break
        k.append(targets)
    def geolocatorf():
        from geopy.geocoders import Nominatim
        geolocator = Nominatim(user_agent="my_python_app")
        location = geolocator.geocode(k)
        print(location.address)
        print(location.latitude, location.longitude)
    return geolocatorf()

def timer():
    import datetime
    n = datetime.datetime.now()
    print(n)



if __name__ == "__main__":
    print(n())
    t()
    timer()
