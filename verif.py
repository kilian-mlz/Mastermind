import random

def verif(code: list, guess: list) -> list:
    """
    Verify the player guess against the secret code.

    Parameters:
    - code (list): The secret code to be guessed.
    - guess (list): The player's guess.

    Returns:
    - list: A list indicating the correctness of each guessed position.
            'G' for correct color and position, 'M' for correct color in the wrong position,
            and '.' for incorrect guess.
    """

    # Initialize an empty list to store the correctness of each guessed position
    mg_liste = ["", "", "", ""]

    # Define the set of valid input colors
    valid_input = set("RGBY")

    # Check if the guess contains only valid colors (RGBY)
    if set(guess) - valid_input:
        print("Invalid input. Please enter only the letters RGBY.")
        return mg_liste

    # Check for correct color and position (marked as 'G')
    for i in range(4):
        if guess[i] == code[i]:
            mg_liste[i] = "G"

    # Check for correct color in the wrong position (marked as 'M')
    for i in range(4):
        if guess[i] != code[i] and guess[i] in code:
            index = code.index(guess[i])
            while mg_liste[index] == "G" or (mg_liste[index] == "M" and code[index:].count(guess[i]) <= guess.count(guess[i])):
                try:
                    index = code.index(guess[i], index + 1)
                except ValueError:
                    break
            if mg_liste[index] != "G":
                mg_liste[index] = "M"

    # Fill in the remaining positions with '.' for incorrect guesses
    for i in range(4):
        if mg_liste[i] == "":
            mg_liste[i] = "."

    # Shuffle the list to randomize the order of 'G', 'M', and '.' for display
    random.shuffle(mg_liste)

    # Return the final list
    return mg_liste
