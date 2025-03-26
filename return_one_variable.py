class X(object):
    def __init__(self):
        self.y = input("Enter a value: ")
    def get_variable(self):
        return self.y


instantiation = X()
instantiation.get_variable()
