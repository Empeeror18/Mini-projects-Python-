from random import randint

lower_num, higher_num = 1, 100
random_num : int = randint(lower_num, higher_num)
print(f"Guess the number between {lower_num} and {higher_num}!")

while True: #Creates an infinite loop
    try:
        user_num = int(input("Enter your guess: "))
    except ValueError as e:
        print ("Enter a valid number!")
        continue

    #Check the number
    if user_num < random_num:
        print("Entered number is too low!")
    elif user_num > random_num:
        print("Entered number is too high!")
    else:
        print("You guessed it!!!")
        break