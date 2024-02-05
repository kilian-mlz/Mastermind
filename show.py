import os
from termcolor import colored
from gamemode import *

def clean_terminal() -> None:
    """
    Clear the terminal screen.

    Returns:
    - None
    """
    os.system("cls")


def rules() -> str:
    """
    Display the rules of the Mastermind game.

    Returns:
    - None
    """

    os.system("cls")
    print("Welcome to Mastermind!")
    print("You must find the code that is composed of 4 colors.")
    print("Possible colors are", colored("Red,", 'red') ,colored("Green,", 'green'),colored("Blue,", 'blue'),colored("Yellow", 'yellow'))
    print("On both sides of the board are randomly ordered indicators:")
    print("G for good colors")
    print("M for misplaced colors")

def display_board(board: list) -> str:
    """
    Display the game board, including the current state of guesses and indicators.

    Parameters:
    - board (list): The game board.

    Returns:
    - None
    """

    print("You must find the code that is composed of 4 colors.")
    print("Possible colors are", colored("Red,", 'red') ,colored("Green,", 'green'),colored("Blue,", 'blue'),colored("Yellow.", 'yellow'))
    print("On both sides of the board are randomly ordered indicators:")
    print("G for good colors")
    print("M for misplaced colors")
    for row in board:
        print(" ".join(row))
    print()
    
