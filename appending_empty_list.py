def function():
	"""
	The function also sorts the list elements
	"""
	empty_list = []
	while True:
			new_var = input("Enter weapons. Press enter to end: ")
			if len(new_var) == 0:
				break
			empty_list.append(new_var)
	empty_list.sort() # return same level after indentation is not real
	def a():
		if len(empty_list) == 1:
			print(f"Show {len(empty_list)} element of the list: "+ str(empty_list))
		else:
			print(f"Show {len(empty_list)} elements of the list: " + str(empty_list))
	a()
function()
