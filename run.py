# Import statements I created for the game
from words import easy_words
from words import hard_words
from hangman_art import hangman_pics

# External imports
import random
import os
import sys

# Welcome message
print("Welcome to Hangman. Test your word knowledge and see if you can avoid the noose! Guess the word and win.\n")

def clear_console():
    """
    Clears the terminal
    Credit - clear console code used from https://www.delftstack.com/howto/python/python-clear-console/ 
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
            raise ValueError("invalid input. Please type your name e.g. John \n")
        elif len(name) == 0:
            raise ValueError("invalid input. Please type your name e.g. John \n")

    except ValueError as error:
        print(f"Try again, {error}")
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
        player_option = int(input("Please enter your option from the above menu: "))
        if player_option == 1:
            select_word()
        elif player_option == 2:
            instructions()
        elif player_option == 0:
            print("Thanks for playing, game exited.")
            print("If you'd like to start over, please press the run program button.")
            sys.exit(0)
        else:
            print("Invalid option. Please choose a valid option from menu")

def select_word():
    """
    Select a random word from either the easy 
    or hard list dependinng on player input
    """
    while True:
        difficulty = int(input("Enter 1 for easy and 2 for hard: "))

        if difficulty == 1:
            word = random.choice(easy_words)
        elif difficulty == 2:
            word = random.choice(hard_words)
        else:
            print("Invalid option. Please select your difficulty.")

def instructions():
    """
    Hangman game instructions
    """
    print("How to play:\n")
    print("1. The aim of the game is to correctly guess the secret word.\n")
    print("2. You will have 7 lives so you need to guess the correct word in this time.\n")
    print("3. To guess the word, type in the letter you wish to guess and hit enter.\n")
    print("4. If you've chosen correctly, then your letter will appear on the screen.\n")
    print("5. If you are wrong then the Hangman will start to appear.\n")
    print("6. The more incorrect guess, the more partd of the Hangman will appear until its GAMEOVER.\n")

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



def main():
    """
    Run all game functions
    """
    player_name()
    menu()
    select_word()


main()
