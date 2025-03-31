class Descriptor:
    def __get__(self, instance, owner):
        print("Getting value")
        return instance._value
    def __set__(self, instance, value):
        print("Setting value")
        instance._value = value

class MyClass:
    attribute = Descriptor() # descriptor instance as class attribute
    def __init__(self, value):
        self.attribute = value # triggers __set__()


obj = MyClass(10) # __set__.Setting value
print(obj.attribute) # __get__.Getting value
