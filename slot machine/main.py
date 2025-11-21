import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "💎" : 2,
    "🍗" : 4,
    "🎀" : 6,
    "💸" : 8
}

def sm_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)

        columns.append(column)
    return columns



def deposit():
    while True:
        amount = input("Enter the amount to be deposited: $")
        if amount.isdigit():
            amount = int(amount)
            if amount < 0:
                print ("Amount must be greater than 0.")
            else:
                break
        else:
            print("Enter a valid number!")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter the number in range.")

        else:
            print("Enter a number!")
    return lines

def get_bets():
    while True:
        bet = input("How much would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter a amount between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Enter a Valid amount")
    return bet



def main():
    amount = deposit()
    lines = get_number_of_lines()
    bet = get_bets()

main()