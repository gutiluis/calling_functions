import random


books = [
        "Automate the Boring Stuff with Python",
        "Python for Data Analysis",
        "Fluent Python",
        "Python for kids",
        "Hello Web App",
]

print("Suggested gift: {}".format(books[0]))

random.shuffle(books)
#print(f"\n{books}")

def x(books):
    r = random.choice(books)
    print(f"\nOnly one from the list: {r}")


x(books)
def c(books):
    n = random.sample(books, 2)# get 2 random items from the list
    return f"\n{len(n)} random items from the list: {n}"


print(c(books))
