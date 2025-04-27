from constants import Targets
import datetime
import random


def display_attack(display_name, missions):
	items = missions.copy()
	print(display_name + ":")
	suggested_attack = random.shuffle(items)
	item = items.pop()
	print("="*10, ">", item, "<", "="*10)
	for i in items:
		print("* " + i)
	print()



display_attack("Next Death Attack", Targets)
