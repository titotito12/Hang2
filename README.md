

# Hang2



Hangman Project.
The peoject is to create a Hangman games where users are prompt to enter a letter from the list  and guess the word.
i am learning about the structure of the project like the random and the list of letters.
Installation instructions :- I created github account and created a Repository in github called Hang2. I then clone the Github repository into my Local folder. I created hangman.py and wordlist.txt.
Hangman is a  game that a player input  a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

Milestone 1
Step 1:- is setting up the GitHub repository for the Hangman Project.
This entails creating the necessary files and documents that showcase professional documentation habitse.g Readme.md file that outline all the steps taken so that there will be clarity and easy to understand for peers and those who will collaborate or use the code for reuse or for other project.


Milestone 2
Created a list containing the name of 5 fruits and assigned the list to the variable word_list.
With the use of the module random, a random word is selected from the list.
The user is asked to input a single letter.
Conditional checks are created that must be passed before the input is accepted.


Milestone 3
To define the functions check_guess and ask_for_input for the Hangman game, 

Step1:- I defined the check_guess function which takes a guessed letter as a parameter and checks if the letter is in the secret word. I passed the guess as a parameter to the function and converted it to lowercase to ensure that the game is case-insensitive.
Step2:- I defined the ask_for_input function which is responsible for asking the user to guess a letter, checking if the input is valid, and checking if the guess is in the secret word. The function will continue to ask for input until a valid guess is made.
Step3:-I also called the check_guess function from within the ask_for_input function to check if the guess is in the secret word. The check_guess function takes the guess as a parameter.
Step4:- I called the ask_for_input function outside the function definition to test the code.


Milestone 4
Class Definition
The Hangman class is defined in the milestone_4 file with the following attributes:

word_list: A list of words from which the game selects a random word.
num_lives: The number of lives the player has to guess the word. Default value is 5.
list_of_guesses: A list that stores the letters guessed by the player.

The class also has the following methods:
__init__(self, word_list, num_lives=5): The initializer method that sets up the game. It takes the word_list and num_lives as parameters, where word_list is a list of words and num_lives is an optional parameter with a default value of 5. It initializes the attributes word, word_guessed, num_letters, and assigns a random word from word_list to word.
check_guess(self, guess): A method that checks if the guessed letter is in the word. It takes a guess parameter and compares it to the letters in the word. If the guess is correct, it updates the word_guessed list and decreases the num_letters count. If the guess is incorrect, it reduces the num_lives count.
ask_for_input(self): A method that asks the player to input a letter guess. It validates the input and checks if the guess has already been made. If the input is valid and a new guess, it calls the check_guess method and updates the list_of_guesses.
Milestone 5
The milestone_5.py script has been added to provide a complete game execution. It includes the following:

The play_game function: This function takes a word_list as a parameter. It sets the number of lives to 5, creates an instance of the Hangman class, and enters a while loop to continue the game until a game-over or victory condition is met. It calls the ask_for_input method to get the player's guesses and checks for the necessary conditions to break out of the loop. At the end, it prints appropriate messages indicating whether the player won or lost the game.
To play the Hangman Game, run the milestone_5.py script and pass a list of words as an argument to the play_game function. The game will interactively prompt you for letter guesses and provide feedback on the correctness of your guesses.

Example usage:

word_list = ["orange", "pear", "apple", "lemon", "banana"]
play_game(word_list)
