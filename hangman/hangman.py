import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    while len(user_input) > 0:
        word = get_valid_word(words)
        word_letter = set(word) #Letters of the word to guess
        alphabet = set(string.ascii_uppercase) #All the alphabet in upper case
        used_letter = set() #Used letter to guess

        user_input = input("Enter the letter: ").upper()
        if user_input in alphabet - used_letter:
            used_letter.add(user_input)
            if user_input in word_letter:
                word_letter.remove(user_input)

        elif user_input in used_letter:
            print("You have already used this character!Try again.")

        else:
            print("Invalid character!")

hangman()