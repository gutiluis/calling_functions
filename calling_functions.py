# *args and **kwargs calling functions
def function(a, b, c):
    print("1.-", a)
    print("2.-", b)
    print("3.-", c)


unpack = ("first value", "second value", "third value")
function(*unpack)
