# decorators modify behavior of functions or methods
# use for logging, authentication and input validation

# decorators take functions as arguments and extend or alter behavior, returning a new function

def simple_decorator(func):
    def wrapper():
        print(f"Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


#apply the decorator to a function
@simple_decorator
def say_hello():
    print("Hello!")

say_hello()

# decorating functions with arguments
# when a function accepts arguments, the decorator must be adapted to accept and pass those arguments as well
def decorator_with_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments passed to function: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@decorator_with_arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice", greeting="Hi")
