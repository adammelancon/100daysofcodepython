print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

n1_lower = name1.lower()
n2_lower = name2.lower()

truescore = 0
lovescore = 0

truescore = truescore + n1_lower.count("t")
truescore = truescore + n1_lower.count("r")
truescore = truescore + n1_lower.count("u")
truescore = truescore + n1_lower.count("e")

lovescore = lovescore + n1_lower.count("l")
lovescore = lovescore + n1_lower.count("o")
lovescore = lovescore + n1_lower.count("v")
lovescore = lovescore + n1_lower.count("e")

truescore = truescore + n2_lower.count("t")
truescore = truescore + n2_lower.count("r")
truescore = truescore + n2_lower.count("u")
truescore = truescore + n2_lower.count("e")

lovescore = lovescore + n2_lower.count("l")
lovescore = lovescore + n2_lower.count("o")
lovescore = lovescore + n2_lower.count("v")
lovescore = lovescore + n2_lower.count("e")

score = str(truescore) + str(lovescore)
print(f"Score: {score}")

score = int(score)


if score < 10 or score > 90:
  print(f"Youre score is {score}, you go together like coke and mentos")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together")
else:
  print(f"Your score is {score}")
