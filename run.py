"""
Imports section
"""
# Import statements I created for the game
from words import easy_words
from words import hard_words

# Welcome message
print("Welcome to Hangman. Test your word knowledge and see if you can avoid the noose! Guess the word and win.\n")

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

def main():
    """
    Run all game functions
    """
    player_name()


main()