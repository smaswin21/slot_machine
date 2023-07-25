# importing modules
import random

# details of the user’s money

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "fire" : 2,
    "water": 4,
    "land" : 6,
    "air"  : 8
}

symbol_value = {
    "fire" : 2,
    "water": 4,
    "land" : 6,
    "air"  : 8
}

# check which line the user bets on

def check_wins(columns, lines, bet, values):
    wins = 0
    wins_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            wins += values[symbol] * bet
            wins_lines.append(line + 1)

    return wins, wins_lines

def get_slot_machine(rows, cols, symbols):

    all_symbols = []
    for symbol, symbol_count in symbols.items(): # key and value associated with the dictionary
        for _ in range(symbol_count): # underscore -
            all_symbols.append(symbol) # anonymous variable which is unused in python

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]  # make sure our values don’t exceed. # slice operator : copy of symbols
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


# User’s Deposit Function

def deposit():
    while True: # continually ask the user to enter the deposit money until a valid amount is mentioned.
        amount = input("What is your deposit? : ")
        if amount.isdigit(): # isdigit just helps us determine if the string is a digit
            amount = int(amount) # this allows the digit to convert as an integer.
            if amount > 0: # check - 1
                break
            else:
                print("The amount needs to be greater than 0 ")
        else:
            print("Please enter a number: ")

    return amount

# call the function by its name with a parenthesis at the end.

# Collect the bet from the user
def get_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?  ")
        if lines.isdigit():  # isdigit just helps us determine if the string is a digit
            lines = int(lines) # this allows the digit to convert as an integer.
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines: ")
        else:
            print("Please enter a number: ")

    return lines

# Collect the amount to bet on each line in the machine
def get_bet():

    while True: # continually ask the user to enter the deposit money until a valid amount is mentioned.
        amount = input("What is your bet on each line? : ")
        if amount.isdigit(): # isdigit just helps us determine if the string is a digit
            amount = int(amount) # this allows the digit to convert as an integer.
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET}  -  ${MAX_BET}. ")
        else:
            print("Please enter a number: ")

    return amount

def spin(balance):

    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have sufficient amount  to bet, as your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. The total bet is equal to : ${total_bet}")

    print("Balance :", balance, "Lines :", lines)

    slots = get_slot_machine(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    wins, wins_lines = check_wins(slots, lines, bet, symbol_value)
    print(f"You won : ${wins}.")
    print(f"You won on lines:", *wins_lines)
    return wins - total_bet

def program():
    balance = deposit()
    while True:
        print(f"Current Balance is: ${balance} ")
        answer = input("Press enter to play (q to quit). ")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

program()





