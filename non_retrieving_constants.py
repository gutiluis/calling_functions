class Getter:
    def __get__(self, obj, objtype=None):
        return "string" # value computed on demand

class Makeclass:
    reg_class_attribute = "second_string"
    descriptor_instance = Getter()


instance = Makeclass()
print(instance.reg_class_attribute)
print(instance.descriptor_instance) # __get__ method
