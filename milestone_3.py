import random

word_list = ["orange", "pear", "apple", "lemon", "banana"]


word = random.choice(word_list)


def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word")
    else:
        print(f"Sorry {guess} is not in the word") 


def ask_for_input():
    while True:
        # Step 2
        guess = input("Guess a letter: ")

        # Step 3
        if len(guess) == 1 and guess.isalpha():
            print("Valid guess:", guess)
            break
        else:
        # Step 5
            print("Invalid letter. Please enter a single alphabetical character.")
    check_guess(guess)


ask_for_input()
