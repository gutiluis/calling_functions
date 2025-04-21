# python closure: 
# nested function that has the ability to access variables from its enclosing scope
# even after the outer function has finished executing
import dis

def variable_function():
	weapon = "bazooka"
	if weapon == "bazooka":
		pass
	def formatter():
		print(f"the selected weapon is {weapon!r}.")
		print(f"Attach {repr(weapon)} for battle.")
	return formatter()

variable_function()

def var_funct():
	targ = ["vancouver", "richmond"]
	def formatter():
		# using print removes the quotes
		print(f"Attack {targ[0]} and {targ[1]}.")
	return formatter()
var_funct()

def n():
# removed return
	import decimal # any code after return at same indentation level is not executed
	def x():
		width = 10
		precision = 4
		value = decimal.Decimal("12.34567")
		def formatter():
			# nested fields
			print(f"Result:{value:{width}.{precision}}")
		return formatter()
	x()
n()

def d():
	import datetime
	def a():
		today = datetime.datetime(year=2017, month=1, day=27)
		if today != datetime.datetime.now():
			print(f"{today:%B %d, %Y}")
			print(f"{today=:%B %d, %Y}")
	a()
d()

def ager():
	a = int(input("Enter an age: "))
	return f"Print the hexadecimal value of the age: {a:#0x}"
print(ager())


