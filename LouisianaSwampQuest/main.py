from time import sleep
from subprocess import call

import os
def clear(): os.system('clear') #on Linux System

def wronganswer():
  print("WRONG ANSWER TRY AGAIN!")

def restart():
  sleep(1)
  clear()
  print("-" * 10 + "THE END" + "-" * 10)
  sleep(1)
  clear()
  main()

def main():
  louisiana = '''
88                         88           88                                    
88                         ""           ""                                    
88                                                                            
88  ,adPPYba,  88       88 88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,  ,adPPYYba,  
88 a8"     "8a 88       88 88 I8[    "" 88 ""     `Y8 88P'   `"8a ""     `Y8  
88 8b       d8 88       88 88  `"Y8ba,  88 ,adPPPPP88 88       88 ,adPPPPP88  
88 "8a,   ,a8" "8a,   ,a88 88 aa    ]8I 88 88,    ,88 88       88 88,    ,88  
88  `"YbbdP"'   `"YbbdP'Y8 88 `"YbbdP"' 88 `"8bbdP"Y8 88       88 `"8bbdP"Y8 '''
  swamp = '''
 _____      ____ _ _ __ ___  _ __  
/ __\ \ /\ / / _` | '_ ` _ \| '_ \ 
\__ \\ V  V / (_| | | | | | | |_) |
|___/ \_/\_/ \__,_|_| |_| |_| .__/ 
                            | |    
                            |_|     '''
  quest = '''
                       _   
                      | |  
  __ _ _   _  ___  ___| |_ 
 / _` | | | |/ _ \/ __| __|
| (_| | |_| |  __/\__ \ |_ 
 \__, |\__,_|\___||___/\__|
    | |                    
    |_|                      '''

  print(louisiana)
  print(swamp + quest)
  print("")
  print("Welcome to da swamp!")
  print("Your mission is to stay alive.") 
  print("")




  testone = input("You come upon a dead possum, do you eat the possum? Y/N: ")

  if testone.lower() == "y":
    testonedead = "Awwww dang, you dead bruh!"
    for char in testonedead:
      sleep(0.08)
      print(char, end='', flush=True)
    restart()

  else:
    clear()

  testtwo = input("\nGood answer! However, the possum comes to life and asks if youwant some 'updog'.\nHow do you answer? \nType 'what's updog' or 'huh': ")

  if testtwo.lower() not in ("whats updog?", "what's updog?", "whats updog", "what's updog"):
    testtwodead = "Come on man! Always reply with what's up dog! The possum has killed you!   ...dummy"
    for char in testtwodead:
      sleep(0.05)
      print(char, end='', flush=True)    
    restart()
  else:
    clear()
    
  testthree = input("YES! 'What's updog' is the correct response!\nSuddenly, an alligator comes up behind you. Do you: \n A: Pull his toes. \n B: Poke him in the eye.\n C: Bop him on his noggin.\n > ")

  if testthree.lower() == "a":
    testthreea = "Oh dang son! That gator done did snap you head off! YOU DEAD!"
    for char in testthreea:
      sleep(0.05)
      print(char, end='', flush=True)    
    restart()    

  elif testthree.lower() == "b":
    testthreeb = "Come on baw! Before you can even poke an eye, he snaps you lil hand off.  You now dead!"
    for char in testthreeb:
      sleep(0.05)
      print(char, end='', flush=True)    
    restart() 

  elif testthree.lower() == "c":
    testthreec = "Mais! Cook some rice cher! You done bopped him good good! He dead baw!"
    for char in testthreec:
      sleep(0.05)
      print(char, end='', flush=True)  
    sleep(2)  
    clear()
    print("")
    print("YOU WIN COULLION!!!")
    sleep(2)
    clear()
    main()
    

  else:
    wronganswer()



main()