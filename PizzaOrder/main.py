print("Welcome to Python Pizza Deliveries!")


def ask():
  size = input("What size pizza do you want? S, M, or L? ")
  if ("s" or "m" or "l") not in size.lower():
    print("")
    print("Please enter 'S, M, or L' for your size!")
    print("")
    ask()
  else:
    pass
  add_pepperoni = input("Do you want pepperoni? Y or N ")
  extra_cheese = input("Do you want extra cheese? Y or N ")
  return

ask()
bill = 0

if size.lower() == "s":
  bill = bill + 15
elif size.lower() == "m":
  bill = bill + 20
elif size.lower() == "l":
  bill = bill + 25

if add_pepperoni.lower() == "y":
  if size.lower() == "s":
    bill += 2
  else:
    bill += 3

if extra_cheese.lower() == "y":
  bill += 1
else:
  pass

print(f"Your final bill is: ${bill}")