# implicit inheritance
class Parent(object):
	def implicit(self):
		print("PARENT implicit()")

class Child(Parent):
	pass # empty block

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
