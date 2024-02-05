import random

# List of available colors
colors = ["R", "G", "B", "Y"]

def code_generator() -> list:
    """
    Generate a random secret code for the Mastermind game.

    Returns:
    - list: A list representing the random secret code.
    """
    # Initialize an empty list to store the randomly generated code
    choice_random = []

    # Loop to randomly select a color for each position in the code
    for i in range(4):
        rand = random.choice(colors)
        choice_random.append(rand)

    # Return the randomly generated code
    return choice_random
