rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

# Get R, P, S from user
def getrps(a):
  if a == "x":
    rps = input('R, P, or S? ')
  else:
    rps = a
  if rps.lower() == "r":
    pass
    # print(rock)
    # rps = rock
  elif rps.lower() == "p":
    pass
    # print(paper)
    # rps = paper
  elif rps.lower() == "s":
    pass
    # print(scissors)
    # rps = scissors
  return rps.lower()

rps = getrps("x")
pcrps = getrps(random.choice(["r", "p", "s"]))

# print("You: " + rps)
# print("PC: " + pcrps)

if rps == "r":
  print("You threw ROCK: " + rock)
elif rps == "p":
  print("You threw PAPER: " + paper)
elif rps == "s":
  print("You threw SCISSORS: " + scissors)

if pcrps == "r":
  print("PC threw ROCK: " + rock)
elif pcrps == "p":
  print("PC threw PAPER: " + paper)
elif pcrps == "s":
  print("PC threw SCISSORS: " + scissors)



# see who won!
if rps == "r" and pcrps == "s":
  print("YOU WON!")
elif rps == "p" and pcrps == "r":
  print("YOU WON!")  
elif rps == "s" and pcrps == "p":
  print("YOU WON!")
# check for a tie
elif rps == "r" and pcrps == "r":
  print("TIE!")
elif rps == "p" and pcrps == "p":
  print("TIE!")  
elif rps == "s" and pcrps == "s":
  print("TIE!")
else:
  print("You Lost...")
