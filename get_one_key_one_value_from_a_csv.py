def get_key():
	global store_csv
	store_csv = [{"name": "Neo", "password": "renault"},
		{"name": "trinity", "password": "bazinga"}]
	for index, person in enumerate(store_csv):
		print(f"{index} - {person["name"]}") # name is a keystore_for_loop
get_key()
print("\n")
def return_after_iteration(store_csv):
	store = []
	for i in enumerate(store_csv):
		store.append(i)
		# return store  # partial iteration
	return store # full iteration

c = return_after_iteration(store_csv)
print("From the 2 users select onlye one. And print data: ")
try:
	choice = int(input("> "))
	if choice == 0:
		print(c[0])
	elif choice == 1:
		print(c[1])
	else:
		print("Error.")
except ValueError:
	print("Error. Enter an integer. 1 or 2 only...")
print("Skipping program...")
print("="*50)
print("")
def no_need_to_iterate_to_index(store_csv):
	print("From the 2 users select only one:")
	try:
		choice = int(input("> "))
		if choice == 0:
			print(store_csv[0])
		elif choice == 1:
			print(store_csv[1])
	except ValueError:
		print("Invalid option.")
		print("Skipping program...")
no_need_to_iterate_to_index(store_csv)
print("="*50)
print("")
def return_after_iteration(store_csv):
	for i, j in enumerate(store_csv):
		print(i, j)
return_after_iteration(store_csv)

print("="*50)
def get_one(store_csv):
	for i, p in enumerate(store_csv):
		print(f"{i}- {p}")
get_one(store_csv)
print("="*50)
def get_password_key(store_csv):
	for i, p in enumerate(store_csv):
		print(f"{i}- {p["password"]}") # birthday is a key
get_one(store_csv)
print("="*50)
print("")
def loop_and_get_one(store_csv):
	import sys
	try:
		x = int(input("Enter 0 or 1: "))
		while x != [1, 2]:
			if x == 0:
				print(store_csv[0])
				break
			elif x == 1:
				print(store_csv[1])
				break
		print("End of loop.")
	except ValueError:
		print("Error. Invalid input. try again?")
	print("try again? ")
	choice = input("> ")
	if choice == "yes":
		loop_and_get_one(store_csv)
	elif choice == "no":
		sys.exit()
	elif choice != "yes":
		raise Exception("Only yes and no.")

loop_and_get_one(store_csv)
