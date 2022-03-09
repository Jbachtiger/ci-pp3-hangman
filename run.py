# Import statements I created for the game
from words import easy_words
from words import hard_words
from hangman_art import hangman_pics

# External imports
import random
import os
import sys

# Welcome message
print("Welcome to Hangman. Avoid the noose by guessing the word and win.\n")


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


def player_name():
    """
    Allows the user to input their name
    """
    while True:
        player_data = input("Enter your name: ")

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


def menu():
    """
    Main menu for game
    """
    print("Main Menu: ")
    print("[1] Start Game")
    print("[2] Instructions")
    print("[0] Exit the game")

    while True:
        player_option = input("Please enter your option from the above menu: ")
        if player_option == "1":
            select_word()
        elif player_option == "2":
            instructions()
        elif player_option == "0":
            print("Thanks for playing, game exited.")
            print("To start over press the run program button.")
            sys.exit(0)
        else:
            print("Invalid option. Please choose a valid option from menu")


def select_word():
    """
    Select a random word from either the easy
    or hard list dependinng on player input
    """
    while True:
        difficulty = input("Enter 1 for easy and 2 for hard: ")

        if difficulty == "1":
            word = random.choice(easy_words)
            game(word)
        elif difficulty == "2":
            word = random.choice(hard_words)
            game(word)
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
    print("7. Once the full hangman appears it's GAMEOVER!")

# Option to return to main menu
    while True:
        back = int(input("Enter 0 to return to main menu: "))
        if back == 0:
            clear_console()
            menu()
        else:
            print("Invalid option. Please enter 0 to return to menu.")


def game(word):
    """
    Main game function
    Credit - MJ Codes -  base code logic for function
    amended from his YouTube tutorial, code has been modified
    and extra features/components added to it
    """
    used_letters = []  # keeps track of what letters the player has used
    wrong_guesses = 0  # keeps track of wrong guesses
    current_guess = "-" * len(word)  # creates dashes for each letter in word
    max_wrong = len(hangman_pics) - 1
    attempts = 6

#  Loop allowing player to guess the correct word on last chance
#  Exit loop if correct word has been guessed
    while wrong_guesses < max_wrong and current_guess != word:
        print(hangman_pics[wrong_guesses])
        print("Attempts left: ", attempts)
        print("Used letters: ", used_letters)
        print("Correctly guessed letters: ", current_guess)

#  Allows player to enter letter guess
        guess = input("Enter your letter guess: ").upper()
        clear_console()

#  Checks to see if the letter has already been used
        while guess in used_letters:
            print("You have already used this letter", guess)
            guess = input("Enter your letter guess: ").upper()

# add guessed letter to used_letters list
        used_letters.append(guess)

# check guess
        if guess in word:
            print("That's a correct letter!")

#  Updates secret word revealing correct letters
#  Adds these to a new word with mixed dashes and letters
            new_current_guess = ""
            for letter in range(len(word)):
                if guess == word[letter]:
                    new_current_guess += guess
                else:
                    new_current_guess += current_guess[letter]
            current_guess = new_current_guess
        else:
            print("Incorrect letter")
            wrong_guesses += 1  # increases number incorrect by 1
            attempts -= 1  # decreases number of lives by 1

#  No more guesses left
    if wrong_guesses == max_wrong:
        print(hangman_pics[wrong_guesses])
        print("Attempts left", attempts)
        print("You've been hanged")
        print("The correct word is", word)
        play_again()
    else:
        print("You have won!")
        play_again()


def play_again():
    """
    Gives player choice to play again or exit to the menu.
    """
    while True:
        restart = input("Play again? Enter 1 for Yes or 2 for No: ")

        if restart == "1":
            select_word()
        elif restart == "2":
            menu()
        else:
            print("Invalid input.")


def main():
    """
    Run all game functions
    """
    player_name()
    menu()
    select_word()
    game()


main()
