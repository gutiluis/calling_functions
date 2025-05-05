# self.index
# self.data

y = input("Enter a path: ")
x = input("Enter something to reverse with a generator iterator: ")

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

# use a string
for char in reverse(x):
    with open(y, "a") as file:
        file.write(char + "\n")


