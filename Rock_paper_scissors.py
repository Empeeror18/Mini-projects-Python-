import random

#Set constants and variable
ROCK = "r"
PAPER = "p"
SCISSORS = "s"
emoji = {ROCK : "🤘", PAPER : "📜", SCISSORS: "✂"}
choice = tuple(emoji.keys())

#Ask for user input
def get_user_choice():
    while True:
        user_choice= input("Choose (r/p/s):").lower()
        if user_choice not in choice:
            print("Enter a valid choice!")
        else:
            return user_choice

#Display the choice of user and computer
def display_choices(user_choice,computer_choice):
    print(f"You choose {emoji[user_choice]}")
    print(f"Computer choose {emoji[computer_choice]}")

#Caclulation and print
def calculate_result(user_choice,computer_choice):
    if ((computer_choice == ROCK and user_choice == SCISSORS) or
        (computer_choice == PAPER and user_choice == ROCK) or
        (computer_choice == SCISSORS and user_choice == PAPER)):
            print("You win!")
    elif (computer_choice == user_choice):
        print("Tie!")
    else:
        print("You loose!")

#Main function
def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choice)
        display_choices(user_choice, computer_choice)
        calculate_result(user_choice, computer_choice)

        print("Press any key to continue")
        cont = input("Do you wish to continue?(y/n): ")
        if cont == "n":
            print("Thank you for playing!")
            return False

play_game()