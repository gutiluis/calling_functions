def get_one():
	global store_csv
	store_csv = [{"name": "Neo", "birthday": "1995-10-22"},
		{"name": "trinity", "birthday": "1991-09-12"}]
	for index, person in enumerate(store_csv):
		print(f"{index} - {person["name"]}") # name is a keystore_for_loop
get_one()

def return_after_iteration(store_csv):
	store = []
	for i in enumerate(store_csv):
		store.append(i)
		# return store  # partial iteration
	return store # full iteration

c = return_after_iteration(store_csv)
choice = int(input("> "))
if choice == 0:
	print(c[0])



print("")
def get_one(store_csv):
	for i, p in enumerate(store_csv):
		print(f"{i}- {p}")
get_one(store_csv)
print("")
def get_one(store_csv):
	for i, p in enumerate(store_csv):
		print(f"{i}- {p["birthday"]}") # birthday is a key
get_one(store_csv)
