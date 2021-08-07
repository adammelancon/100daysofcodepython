# Split string method
names_string = input("Give me everybody's names, separated by a comma. \n > ")
names = names_string.split(", ")

import random

entries = len(names)
pickrand = random.randint(0, entries)
# print(names)
# print(entries)

print("The sucker is: " + names[pickrand])

