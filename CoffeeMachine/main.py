import os
from time import sleep

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 500,
    "money": 0.00,
}

# LOW RESOURCES TEST
# resources = {
#     "water": 0,
#     "milk": 0,
#     "coffee": 0,
#     "money": 0.00,
# }
# ========================================================================


def round_money(x):
    '''rounds money to two decimals with trailing zeros'''
    x = '{:.2f}'.format(round(float(x), 2))
    return x


def clear_screen():
    '''Clears the screen'''
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # It is for Windows platfrom
        _ = os.system('cls')


def error_msg(em):
    '''Takes either ("no_resources") or ("not_enough_money") to print error message for each.'''
    if em == "no_resources":
        print(
            "      Not enough resources. \nPlease choose something different.")
        print("")
        print("-----------Press Enter To Continue----------------")
        input("")
        take_order()
    if em == "not_enough_money":
        print(
            "      You Didn't Enter Enough Money. \nPlease choose something different."
        )
        print("")
        print("-----------Press Enter To Continue----------------")
        input("")


def print_resources():
    '''Prints a list of the machine's resources.'''
    clear_screen()
    print("-------------------------------------------------")
    print("----------------Resources------------------------")
    print("-------------------------------------------------")
    print(f" Water: {resources['water']} ml")
    print(f"  Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f" Money: ${round_money(resources['money'])}")
    print("--------------------------------------------------")
    print("-----------Press Enter To Continue----------------")
    input("")


def add_resources():
    clear_screen()
    print("-------------------------------------------------")
    print("-----------ADD Resources Menu--------------------")
    print("-------------------------------------------------")
    print(f" Water: {resources['water']} ml")
    print(f"  Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f" Money: ${round_money(resources['money'])}")
    print("--------------------------------------------------")
    add_what = input(
        "What are you adding? [W]ater / [M]ilk / [C]offee / [E]xit: ").lower()
    if add_what == "w":
        resources['water'] = resources['water'] + int(
            input("Enter water amount in ml: "))
        add_resources()
    elif add_what == "m":
        resources['milk'] = resources['milk'] + int(
            input("Enter milk amount in ml: "))
        add_resources()
    elif add_what == "c":
        resources['coffee'] = resources['coffee'] + int(
            input("Enter coffee amount in ml: "))
        add_resources()
    elif add_what == "e":
        take_order()


def check_resources(drink_choice):
    '''Takes the drink choice (e, l, or c)'''
    if drink_choice == 'e':
        if MENU['espresso']["ingredients"]['water'] > resources[
                "water"] or MENU['espresso']["ingredients"][
                    'coffee'] > resources["coffee"]:
            error_msg("no_resources")
        else:
            print("=================")
            print("Espresso Chosen")
            process_payment(drink_choice)
    elif drink_choice == 'l':
        if MENU['latte']["ingredients"]['water'] > resources["water"] or MENU[
                'latte']["ingredients"]['coffee'] > resources["coffee"] or MENU[
                    'latte']["ingredients"]['milk'] > resources["milk"]:
            error_msg("no_resources")
        else:
            print("=================")
            print("Latte Chosen")
            process_payment(drink_choice)
    elif drink_choice == 'c':
        if MENU['cappuccino']["ingredients"]['water'] > resources[
                "water"] or MENU['cappuccino']["ingredients"][
                    'coffee'] > resources["coffee"] or MENU['cappuccino'][
                        "ingredients"]['milk'] > resources["milk"]:
            error_msg("no_resources")
        else:
            print("=================")
            print("Cappuccino Chosen")
            process_payment(drink_choice)
    elif drink_choice == "r":
        print_resources()
        take_order()
    elif drink_choice == "add":
        add_resources()
    elif drink_choice == "off":
        exit(1)


def process_payment(which_drink):
    '''Gets payment owed based on drink. Then takes money from customer and provides change or rejects due to lack of funds.'''
    global resources
    # Get prices for each drink.
    if which_drink == "e":
        price = float(MENU['espresso']['cost'])
    elif which_drink == "l":
        price = float(MENU['latte']['cost'])
    elif which_drink == "c":
        price = float(MENU['cappuccino']['cost'])
    # Tell customer the cost
    print(f"Please pay: ${round_money(price)}")
    print("=================")
    print("")
    # Calculate money received from customer.
    money_taken = float(take_money())
    # Check if enough money was given.
    if money_taken < price:
        # Return money to customer from register
        resources['money'] = float(resources['money']) - money_taken
        error_msg("not_enough_money")
        take_order()  # NOT ENOUGH MONEY, START OVER
    elif money_taken >= price:
        # Calculate change to give back.
        change = money_taken - price
        # Remove change given from register total.
        resources['money'] = float(resources['money']) - change
        # Print on-screen receipt.
        print(f"  Paid: ${round_money(money_taken)}")
        print(f" Price: ${round_money(price)}")
        print(f"         ----")
        print(f"Change: ${round_money(change)}")
        # Debug print to show register total.
        print(f"Reg $$: ${round_money(resources['money'])}")
        # All paid up! Move forward and make the drink.
        make_drink(which_drink)
    else:
        print("Thanks!")


def take_money():
    '''Accepts money from customer and returns how much they put in the machine.'''
    global resources
    print("Enter Your Payment:")
    print("-------------------")
    # TODO sanity check for money input, no non-int characters.
    quarters = float(input("Number of Quarters? ")) * float(0.25)
    dimes = float(input("Number of Dimes? ")) * float(0.10)
    nickles = float(input("Number of Nickles? ")) * float(0.05)
    pennies = float(input("Number of Pennies? ")) * float(0.01)
    print("-------------------")
    print("")
    clear_screen()
    # Calculate total money given and add to register.
    total_pay = quarters + dimes + nickles + pennies
    resources['money'] = float(resources['money']) + float(
        round_money(total_pay))
    # Go back to process_payment
    return total_pay


def print_menu():
    '''Prints the drink menu.'''
    clear_screen()
    print("---------------------------")
    print("☕  MR COUGHY - MENU ☕")
    print("---------------------------")
    print(f"  Espresso: ${MENU['espresso']['cost']}0")
    print(f"     Latte: ${MENU['latte']['cost']}0")
    print(f"Cappuccino: ${MENU['cappuccino']['cost']}0")
    print("")


def take_order():
    '''Asks for the order from the customer.'''
    print_menu()
    # Hidden are the options [r] for report, [off] for power down, and [add] for adding resources.
    order = input(
        "​What would you like? [E]spresso / [L]atte / [C]appuccino: ").lower()
    # Comment above and uncomment below for quick testing.
    # order = "e"
    # Check to see if we have enough resources.
    check_resources(order)


def make_drink(drink_type):
    '''This takes the drink type "e" "l" or "c" as input and makes it while deducting from resources.'''
    print(f"Making your Drink!")
    sleep(3)
    if drink_type == 'e':
        resources['water'] = resources['water'] - MENU['espresso'][
            "ingredients"]['water']
        resources['coffee'] = resources['coffee'] - MENU['espresso'][
            "ingredients"]['coffee']
        print("Enjoy Your Espresso! ☕")
        sleep(5)
        take_order()
    if drink_type == 'l':
        resources['water'] = resources['water'] - MENU['latte']["ingredients"][
            'water']
        resources[
            'milk'] = resources['milk'] - MENU['latte']["ingredients"]['milk']
        resources['latte'] = resources['coffee'] - MENU['latte'][
            "ingredients"]['coffee']
        print("Enjoy Your Latte! ☕")
        sleep(5)
        take_order()
    if drink_type == 'c':
        resources['water'] = resources['water'] - MENU['cappuccino'][
            "ingredients"]['water']
        resources['milk'] = resources['milk'] - MENU['cappuccino'][
            "ingredients"]['milk']
        resources['latte'] = resources['coffee'] - MENU['cappuccino'][
            "ingredients"]['coffee']
        print("Enjoy Your Cappuccino! ☕")
        sleep(5)
        take_order()


clear_screen()
take_order()

# DONE Prompt User with "​What would you like? ( [E]spresso/[L]atte/[C]appuccino )"
# DONE create "off" command to shut it down
# DONE cretae "report" command to print report
# DONE check resources before making coffee
# DONE process coins for the payment and give change or tell not enough for drink
# DONE deduct from resources when making coffee
# DONE Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
