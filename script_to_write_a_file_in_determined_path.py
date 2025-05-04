#path = input("Enter the path and file name: ")

y = input("Enter the text: ")




def write_file(path, y):
	path = "/media/ltest/python/builtinfunctions/min/min.py"
	with open(path, "a") as file:
		file.write(y + "\n")
		file.close()


write_file(path, y)
