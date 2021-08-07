#Step 5

import random
import hangman_words
import hangman_art

debug = False

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')
# print(f"The word has {word_length} letters")

#Create blanks
display = []

for _ in range(word_length):
    display += "_"

already_guessed = []


def checkscore():
  if lives == 0:
    global end_of_game
    end_of_game = True
    print (u"{}[2J{}[;H".format(chr(27), chr(27)), end="")
    print(hangman_art.logo)
    print("")
    print("           YOU LOOSE! GAME OVER!")
    print("")
    print(f"         The secret word was {chosen_word}")
    

while not end_of_game:
  if debug == True:
    print(f'Pssst, the solution is {chosen_word}.')
  print("")
  print(f"You have {lives} lives.")
  print(f"The word has {word_length} letters")
  print(f"{' '.join(display)} <- Word To Guess")

  print("")
  guess = input("Guess a letter: ").lower()
  print (u"{}[2J{}[;H".format(chr(27), chr(27)), end="")
  # print(f"You guessed: {guess}")
      #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
  if not guess in chosen_word and not guess in already_guessed:
    lives -= 1
    checkscore()
    print(f"The letter '{guess}' is WRONG.")
    print("")
  elif not guess in already_guessed:
    print(f"The letter '{guess}' is CORRECT.")
    
  if not end_of_game and guess in already_guessed:
    print(f"You Already Guessed: {guess}")
  elif not end_of_game and guess not in already_guessed:
    already_guessed.append(guess)
    print(f"Previous Guesses: {', '.join(already_guessed)}")
    print("")

  # print("~~" * 10)

  #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
      display[position] = letter
  
  #Check if user is wrong.
  
  #Join all the elements in the list and turn it into a String.


  #Check if user has got all letters.
  if "_" not in display:
      end_of_game = True
      #print (u"{}[2J{}[;H".format(chr(27), chr(27)), end="")
      print(hangman_art.logo)
      print(f"{' '.join(display)}")
      print("You win.")

  #TODO-2: - Import the stages from hangman_art.py and make this error go away.
  print(hangman_art.stages[lives])
  checkscore()
  