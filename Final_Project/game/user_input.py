import tkinter as tk
from tkinter import simpledialog


def get_user_input():
    """
    Opens a separate window to collect the user's name and the number of cards to play.
    Includes error handling for invalid input.
    Returns a tuple: (name, num_cards).
    """
    # Initialize the tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt for the player's name
    name = simpledialog.askstring("Player Name", "Enter your name:")
    if not name:
        name = "Player"  # Default name if none is entered

    # Prompt for the number of cards to play
    num_cards = None
    while True:
        try:
            num_cards = simpledialog.askinteger(
                "Number of Cards",
                "Enter # of Cards to Play (8, 10, 12):",
            )
            if num_cards in [8, 10, 12]:
                break  # Valid input, exit the loop
            else:
                raise ValueError
        except (ValueError, TypeError):
            tk.messagebox.showerror(
                "Invalid Input", "Please enter a valid number: 8, 10, or 12."
            )

    return name, num_cards
