from art import *
import replit

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(start_text, shift_amount, cipher_direction):

    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if shift_amount >= 26:
            newshift = 26 - (shift_amount % 26)
            print(newshift)
            shift_amount = newshift
        if char == " ":
            end_text += " "
        elif char.isnumeric():
            end_text += char
        elif not char.isalpha():
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}")

    restart = input("Want to do another Y/N?")
    if restart.lower() == "y":
        begin()
    else:
        quit()


def begin():
    replit.clear()
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

begin()
