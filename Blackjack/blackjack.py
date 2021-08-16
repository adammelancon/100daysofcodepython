import random
import time
from os import system
#DONE# The deck is unlimited in size. 
#DONE# There are no jokers. 
#DONE# The Jack/Queen/King all count as 10.
#DONE# The the Ace can count as 11 or 1.
#DONE# Use the following list as the deck of cards:
#DONE# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#DONE# The cards in the list have equal probability of being drawn.
#DONE# Cards are not removed from the deck as they are drawn.
#DONE# The computer is the dealer.
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
# TODO: If player 1 says no more cards, figure out code for 
# dealer choices to pick more than one cards. 

system('cls')
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []
player_hand_total = 0
dealer_hand_total = 0
player_turn = "p"
current_players_name = "Player"
count = 0


def reset_game():
    global player_hand
    global dealer_hand
    global player_hand_total
    global dealer_hand_total
    global player_turn
    global current_players_name 
    global count
    player_hand = []
    dealer_hand = []
    player_hand_total = 0
    dealer_hand_total = 0
    player_turn = "p"
    current_players_name = "Player"
    count = 0


def flip_turn():
    global player_turn
    global current_players_name
    
    if player_turn == "p":
        # print("")
        # print("Flipping player to Dealer")
        # print("")
        player_turn = "d"
        current_players_name = "Dealer"
    elif player_turn == "d":
        # print("Flipping player to Player")
        player_turn = "p"
        current_players_name = "Player"
    # print(f'player_turn variable now = {player_turn}')
    # print(f'Player flipped to: {current_players_name}')
    # print("")
    #input("continue...")
    run_turn(player_turn)


def check_ace_or_one(check_card):
    lc = last_card
    if check_card == 11:
        if check_card + 11 > 21:
            return 1
        else:
            return 11


def check_winner():
    if player_hand_total > dealer_hand_total:
        # clear_and_show_info()
        print("Player has the higher cards! You Win!")
        print("")
        print(f'Total: {player_hand_total} - Player hand: {player_hand}')
        print(f'Total: {dealer_hand_total} - Dealer hand: {dealer_hand}')
        print("")
        play_again()
    else:
        # clear_and_show_info()
        print("Dealer has the highest cards! Dealer wins!")
        print("")
        print(f'Total: {player_hand_total} - Player hand: {player_hand}')
        print(f'Total: {dealer_hand_total} - Dealer hand: {dealer_hand}')        
        print("")
        play_again()


def clear_and_show_info():
        system('cls')
        print(logo)
        show_hands()


def grab_a_card(player):
    global player_hand_total
    global dealer_hand_total
    new_pick = random.choice(cards)
    if player == "p":
        hand = player_hand_total
    elif player == "d":
        hand = dealer_hand_total

    if new_pick == 11:
        if (hand + 11) >= 22:
            return int(1)
        else:
            return int(11)
    else:
        return new_pick


def deal_first_hand():
    global dealer_hand
    global player_hand
    for i in range(0,1):
        player_hand.append(grab_a_card("p"))
        dealer_hand.append(grab_a_card("d"))
        player_hand.append(grab_a_card("p"))
        dealer_hand.append(grab_a_card("d"))
    print("")
    last_card()
    print(f"{current_players_name}'s Turn.")
    print("")


def deal_hand(player):
    clear_and_show_info()
    global dealer_hand
    global player_hand
    global count
    # print(f'deal_hand was handed player {player}')
    if player == "p":
        print("Player's Turn")
        print("")
        player_hand.append(grab_a_card("p"))
        show_hands()
        blackjack_or_bust()
    elif player == "d" and count <= 1:
        # print("Dealer's Turn")
        # print("")
        if dealer_hand_total >= 16:
            count += 2
            flip_turn()  # THIS WAS THE BUG!!! IT WAS SET TO DEAL TO p INSTEAD OF flip_turn()
            print("Dealer passed, card were more than 16")
            # input("c")
        elif dealer_hand_total <= 15:
            print("Dealer is under 16, takes another card.")
            count += 1
            # input("c")
            dealer_hand.append(grab_a_card("d"))
            show_hands()
            blackjack_or_bust()
        show_hands()
        blackjack_or_bust()
    else:
        check_winner()



def show_hands():
    global player_hand_total
    global dealer_hand_total
    player_hand_total = sum(player_hand)
    dealer_hand_total = sum(dealer_hand)
    print("")
    print("")
    print(f'Total: {player_hand_total} - Player hand: {player_hand}')
    # print(f'Total: {dealer_hand_total} - Dealer hand: {dealer_hand}')
    print(f'Dealer visible card: {dealer_hand[1]}')

    print("")


def blackjack_or_bust():
    if player_hand_total == dealer_hand_total:
        clear_and_show_info()
        print("")
        print("TIE!")
        print("")
        print(f'Total: {player_hand_total} - Player hand: {player_hand}')
        print(f'Total: {dealer_hand_total} - Dealer hand: {dealer_hand}')
        print("")        
        play_again()
    elif player_hand_total >= 22 or dealer_hand_total >= 22:
        show_hands()
        if player_hand_total >= 22:
            clear_and_show_info()
            print("")
            print(f"BUSTED! You went over 21!")
            print("")
            print(f'Total: {player_hand_total} - Player hand: {player_hand}')
            print(f'Total: {dealer_hand_total} - Dealer hand: {dealer_hand}')
            print("")            
            play_again()
        elif dealer_hand_total >= 22:
            clear_and_show_info()
            print("")
            print(f"YOU WON! Dealer went over 21!")
            print("")
            print(f'Total: {player_hand_total} - Player hand: {player_hand}')
            print(f'Total: {dealer_hand_total} - Dealer hand: {dealer_hand}')
            print("")            
            play_again()
    elif dealer_hand_total == 21:
        clear_and_show_info()
        print("")
        print(f"YOU LOST! Dealer got Blackjack!")
        print("")
        print(f'Total: {player_hand_total} - Player hand: {player_hand}')
        print(f'Total: {dealer_hand_total} - Dealer hand: {dealer_hand}')
        print("")        
        play_again()
    elif player_hand_total == 21:
        clear_and_show_info()
        print("")
        print(f"YOU WON!  YOU GOT BLACKJACK!!")
        print("")
        print(f'Total: {player_hand_total} - Player hand: {player_hand}')
        print(f'Total: {dealer_hand_total} - Dealer hand: {dealer_hand}')
        print("")        
        play_again()
    else:
        print(".")
        print("")
        run_turn(player_turn)
        

def last_card():
    if player_turn == "p":
        latest_card = player_hand[-1]
        print(f"{current_players_name}'s newest card: {latest_card}")
        return latest_card
    elif player_turn == "d":
        latest_card = dealer_hand[-1]
        print(f"{current_players_name}'s newest card: {latest_card}")  
        return latest_card      


def run_turn(player):
    if player == "p": 
        print(f'Your Total: {player_hand_total}')
        # print("Another Card = n")
        another = input("Another Card? y/n: ").lower()
        if another == "y":
            deal_hand(player)
        elif another == "n":
            flip_turn()
    elif player == "d":
        deal_hand(player)
        

def play_again():
    doyou = input("Do you want to play again? y/n: ").lower()
    if doyou == "y":
        reset_game()
        system('cls')
        begin()
    elif doyou == "n":
        input("GAME OVER") 


def begin():
    print(logo)
    deal_first_hand()
    show_hands()
    blackjack_or_bust()

begin()