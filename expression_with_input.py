def check_path():
    import os
    file_path = input("Enter file name: ")
    os.path.exists(file_path) and print("File exists!") or print("File does not exist")

check_path()
def a():
    a = input("Enter username: ") or "guest"
    b = input("Enter password: ") or "no password"
    c = {a: b}
    print(c)
a()

def n():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    g = "no password"
    b = "guest"
    c = username or b
    e = password or g
    print("Welcome", c)
    print("The password:", e)
n()

def dictionary_key_access_with_default():
    data = {"name": "Alice"}
    user_age = data.get("age") or "Unknown"
    print(f"User age: {user_age}")

dictionary_key_access_with_default()
