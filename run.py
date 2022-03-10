# Import statements I created for the game
from words import easy_words, hard_words
from hangman_art import hangman_pics

# External imports
import random
import os
import sys


def clear_console():
    """
    Clears the terminal
    Credit - clear console code used from
    https://www.delftstack.com/howto/python/python-clear-console/
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def take_player_name_input():
    """
    Allows the user to input their name
    """
    while True:
        player_data = input("Enter your name: \n")

        if validate_player_name(player_data):
            print(f"Welcome to Hangman {player_data} \n")
            break


def validate_player_name(name):
    """
    Validate player name input so it cannot be left blank
    """
    try:
        if name == "":
            raise ValueError("Please type your name e.g. John \n")
        elif len(name) == 0:
            raise ValueError("Please type your name e.g. John \n")

    except ValueError as error:
        print(f"Try again, invalid input. {error}")
        return False

    return True


def show_menu():
    """
    Main menu for game
    """
    print("Main Menu: ")
    print("[1] Start Game")
    print("[2] Instructions")
    print("[0] Exit the game")

    while True:
        player_option = input("Please enter your option from menu: \n")
        if player_option == "1":
            select_random_word()
        elif player_option == "2":
            instructions()
        elif player_option == "0":
            print("Thanks for playing, game exited.")
            print("To start over press the run program button.")
            sys.exit(0)
        else:
            print("Invalid option. Please choose a valid option from menu")


def select_random_word():
    """
    Select a random word from either the easy
    or hard list dependinng on player input
    """
    while True:
        difficulty = input("Enter 1 for easy and 2 for hard: \n")

        if difficulty == "1":
            word = random.choice(easy_words)
            start_game(word)
        elif difficulty == "2":
            word = random.choice(hard_words)
            start_game(word)
        else:
            print("Invalid option. Please select your difficulty.")


def instructions():
    """
    Hangman game instructions
    """
    print("How to play:\n")
    print("1. The aim of the game is to correctly guess the secret word.\n")
    print("2. You have 6 chances to guess the correct word.\n")
    print("3. To guess a letter, type in the letter and hit enter.\n")
    print("4. Correct letters will appear in the secret word.\n")
    print("5. If you are wrong then the Hangman will start to appear.\n")
    print("6. Incorrect guesses make a different part of the hangman show.\n")
    print("7. Once the full hangman appears it's GAMEOVER!\n")

# Option to return to main menu
    while True:
        back = input("Enter 0 to return to main menu: \n")
        if back == "0":
            clear_console()
            show_menu()
        else:
            print("Invalid option. Please enter 0 to return to menu.")


def take_guess_input():
    """
    Function that takes guess input and validates
    to ensure only 1 letter is inputted at a time
    If nothing is inputted an error message shows
    """
    guess = ''
    while not guess.isalpha() and len(guess) != 1:
        guess = input("Enter your letter guess: \n").upper()
        if guess == '':
            print("Enter a valid letter\n")
    return guess


def start_game(word):
    """
    Main game function
    Credit - MJ Codes -  base code logic for function
    amended from his YouTube tutorial, code has been modified
    and extra features/components added to it
    """
    used_letters = []  # keeps track of what letters the player has used
    wrong_guesses = 0  # keeps track of wrong guesses
    current_guess = "-" * len(word)  # creates dashes for each letter in word
    max_wrong_attempts_allowed = len(hangman_pics) - 1  # max attempts before full Hangman pic displays
    lives = 6

#  Loop allowing player to guess the correct word on last chance
#  Exit loop if correct word has been guessed
    while wrong_guesses < max_wrong_attempts_allowed and current_guess != word:
        print(hangman_pics[wrong_guesses])
        print("Attempts left: ", lives)
        print("Used letters: ", used_letters)
        print("Correctly guessed letters: ", current_guess)

#  Allows player to enter letter guess
        guessed_letter = input("Enter your letter guess: \n").upper()
        clear_console()

#  Checks to see if the letter has already been used
        while guessed_letter in used_letters:
            print("You have already used this letter", guessed_letter)
            guessed_letter = take_guess_input()

# add guessed letter to used_letters list
        used_letters.append(guessed_letter)

# check guess
        if guessed_letter in word:
            print("That's a correct letter!")

#  Updates secret word revealing correct letters
#  Adds these to a new word with mixed dashes and letters
            new_current_guess = ""
            for letter in range(len(word)):
                if guessed_letter == word[letter]:
                    new_current_guess += guessed_letter
                else:
                    new_current_guess += current_guess[letter]
            current_guess = new_current_guess
        else:
            print("Incorrect letter")
            wrong_guesses += 1  # increases number incorrect by 1
            lives -= 1  # decreases number of lives by 1

#  No more guesses left
    if wrong_guesses == max_wrong_attempts_allowed:
        print(hangman_pics[wrong_guesses])
        print("Attempts left", lives)
        print("You've been hanged")
        print("The correct word is", word)
        ask_to_play_again()
    else:
        print("You have won!")
        ask_to_play_again()


def ask_to_play_again():
    """
    Gives player choice to play again or exit to the menu.
    """
    while True:
        restart = input("Play again? Enter 1 for Yes or 2 for No: \n")

        if restart == "1":
            select_random_word()
        elif restart == "2":
            show_menu()
        else:
            print("Invalid input.")


def main():
    """
    Run all game functions
    """
    
    print("Welcome to Hangman. Avoid the noose by guessing the word and win.\n")  # Welcome message
    take_player_name_input()
    show_menu()
    select_random_word()
    start_game()


main()
