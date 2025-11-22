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

symbol_values = {
    "💎": 8,
    "🍗": 4,
    "🎀": 2,
    "💸": 1
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

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winnings += values[symbol] * bet

    return winnings

def print_sm(columns):
    rows = len(columns[0])
    print("+-------------------------+")
    for r in range(rows):
        row_items = []
        for col in columns:
            row_items.append(col[r])
        print(" | ".join(row_items))
    print("+-------------------------+")



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

def spin (balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bets()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough credits! Your current balance is {balance}")
        else:
            break

    print(f"You are betting ${balance} on {lines} lines. Your total bet is ${total_bet}.")

    slots = sm_spin(ROWS, COLS, symbol_count)
    print_sm(slots)

    winnings = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}.")
    return winnings


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).").lower()
        if answer == "q":
            break
        balance += spin(balance)

main()