year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 != 0:
    print("yep 100")
  elif year % 400 == 0:
    print("yep 400")
  else:
    print("Nope 3 levels down.")
else:
  print("Nah dog, not a leap year!")


