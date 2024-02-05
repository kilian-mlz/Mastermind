from show import *
from generate_code import *
from gamemode import *
from verif import *

def play(code: list) -> None:
    """
    Execute the game.

    Parameters:
    - code (list): The secret code to be guessed.

    Returns:
    - None
    """
    # Initialize the number of attempts
    attempts = 0
    clean_terminal()  # Clear the terminal screen
    display_board(board)  # Display the initial game board

    # Loop for the maximum number of attempts
    for i in range(8):
        attempts += 1
        while True:
            # Get user input for the guess
            guess = input("Enter your guess: ").upper()
            guess = list(guess)  # Convert the guess to a list of characters
            clean_terminal()  # Clear the terminal screen

            # Validate the guess format (4 characters, each in "RGBY")
            if all(letter in "RGBY" for letter in guess) and len(guess) == 4:
                break
            else:
                print("Invalid input. Please enter a valid guess using only the letters RGBY.")

        # Get the feedback for the guess using the verif function
        mg_liste = verif(code, guess)

        # Update the game board with the guess and its feedback
        board[i + 1] = [mg_liste[0], mg_liste[1], "|", guess[0], guess[1], guess[2], guess[3], "|", mg_liste[2],
                        mg_liste[3]]
        display_board(board)  # Display the updated game board

        # Check if the guess is correct and end the game if it is
        if guess == code:
            print(" --------------------------------------------")
            print(f"| You win in {attempts} attempts ! The code was: {''.join(code)} |")
            print(" --------------------------------------------")
            return

    # If the loop completes without a correct guess, display a losing message
    if guess != code:
        print(" ------------------------------")
        print(f"| You lose, the code was {''.join(code)}. |")
        print(" ------------------------------")
        return

def main() -> None:
    global board, code  # Global variables for the game board and secret code
    restart = True  # Variable to control game restart

    # Loop for restarting the game
    while restart:
        rules()  # Display game rules
        board = [[" ", " ", "|", "?", "?", "?", "?", "|", " ", " "],
                 [".", ".", "|", ".", ".", ".", ".", "|", ".", "."],
                 [".", ".", "|", ".", ".", ".", ".", "|", ".", "."],
                 [".", ".", "|", ".", ".", ".", ".", "|", ".", "."],
                 [".", ".", "|", ".", ".", ".", ".", "|", ".", "."],
                 [".", ".", "|", ".", ".", ".", ".", "|", ".", "."],
                 [".", ".", "|", ".", ".", ".", ".", "|", ".", "."],
                 [".", ".", "|", ".", ".", ".", ".", "|", ".", "."],
                 [".", ".", "|", ".", ".", ".", ".", "|", ".", "."]]

        gamemode_choice = gamemode()  # Choose game mode

        # Computer-generated code mode
        if gamemode_choice == 'c':
            code = code_generator()  # Generate a secret code
            play(code)  # Play the game with the generated code

        # Player-entered code mode
        if gamemode_choice == "p":
            good = True
            while good:
                # Get the code to guess from the player
                code = input("Player 2, enter the code to guess: ").upper()
                code = list(code)
                # Validate the code format (4 characters, each in "RGBY")
                for i in range(4):
                    if code[i] not in colors or len(code) != 4:
                        print("Invalid input, Please enter a valid guess using only the letters RGBY.")
                        break
                    else:
                        good = False
            play(code)  # Play the game with the player's code

        choice = True
        while choice == True:
            # Ask if the player wants to play again
            restart = input("Do you want to play again ? Y/N: ").upper()
            if restart == "N":
                print("Goodbye!")
                restart = False
                choice = False
            elif restart == "Y":
                choice = False
            else:
                print("Invalid input, please enter Y or N.")

if __name__ == "__main__":
    main()
