from show import *
from main import *
from verif import *
from generate_code import *

# Initialize the game board
board = [[" ", " ", "|", "?", "?", "?", "?", "|", " ", " "],
        [".", ".", "|", ".", ".", ".", ".", "|", ".", "."],
        [".", ".", "|", ".", ".", ".", ".", "|", ".", "."],
        [".", ".", "|", ".", ".", ".", ".", "|", ".", "."],
        [".", ".", "|", ".", ".", ".", ".", "|", ".", "."],
        [".", ".", "|", ".", ".", ".", ".", "|", ".", "."],
        [".", ".", "|", ".", ".", ".", ".", "|", ".", "."],
        [".", ".", "|", ".", ".", ".", ".", "|", ".", "."],
        [".", ".", "|", ".", ".", ".", ".", "|", ".", "."]]

def gamemode() -> str:
    """
    Ask the user to select the game mode (computer or player) and return the chosen mode.

    Returns:
    - str: The selected game mode ('c' for computer mode, 'p' for player mode).
    """
    cond = True
    while cond:
        # Ask the user to input the desired game mode
        gamemode = input("Do you want to play against a computer or a player? (C/P): ").lower()

        # Check and print the chosen game mode
        if gamemode == "c":
            print("You chose computer mode!")
            cond = False
        elif gamemode == "p":
            print("You chose player mode!")
            cond = False
        else:
            # Ask the user for valid input if an invalid option is chosen
            print("Invalid input, please enter C or P to continue")

    # Return the selected game mode
    return gamemode
