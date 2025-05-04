def decimal_then_binary():
	# this makes the input a string either way
	x = input("Enter a single letter: ")
	if x.isdigit():
		raise Exception("Do not enter an integer")
	elif not x:
		raise Exception("Enter something")
	elif len(x) > 1:
		raise Exception("Enter only 1 character")
	else:
		make_decimal = ord(x)
		make_binary = bin(make_decimal)
		print(make_binary)


decimal_then_binary()
