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