x = input("Enter something to reverse: ")



def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

# use a string
for char in reverse(x):
	print(char)



