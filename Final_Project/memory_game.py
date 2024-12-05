import turtle
from game.ui import UI  # UI helper for orchestrating layout, status bar, and leaderboard
from game.assets import load_assets  # Handles dynamic asset loading
from game.layout import Layout  # For drawing the layout and quit button
from game.user_input import get_user_input  # For collecting user input
from game.leaderboard import Leaderboard  # Interface for leaderboard logic

def main():
    """
    Entry point for the memory game application.
    Initializes the screen, collects user input, and prepares the game layout.
    """
    # Initialize the screen
    screen = UI.initialize_screen("Memory Match Game", 800, 600)

    # Collect user input
    player_name, num_cards = get_user_input()
    print(f"Welcome, {player_name}! You selected {num_cards} cards to play.")

    # Load all assets dynamically
    assets = load_assets()

    # Example: Dynamically select card images for the game
    card_images = [key for key in assets if key not in ["card_back", "quitbutton"]]
    selected_cards = card_images[:num_cards]
    print(f"Selected cards for the game: {selected_cards}")

    # Draw the static layout
    UI.draw_layout()

    # Add the quit button
    quit_turtle = Layout.add_quit_button(assets["quitbutton"])

    # Initialize the status bar
    status_turtle = UI.draw_status_bar_text(guesses=0, matches=0)

    # Initial leaderboard setup
    player_score = 0  # Player starts with a score of 0
    Leaderboard.draw_leaderboard(player_name, player_score)

    # Example Game Loop
    for turn in range(1, 6):  # Simulate 5 turns
        player_score += 5  # Simulate scoring
        Leaderboard.update_leaderboard(player_name, player_score)  # Update scores
        Leaderboard.draw_leaderboard(player_name, player_score)  # Redraw leaderboard

    # Define quit functionality
    def quit_game(x, y):
        if 150 <= x <= 250 and -200 >= y >= -250:
            print("Quit button clicked. Exiting the game...")
            turtle.bye()

    quit_turtle.onclick(quit_game)

    # Keep the screen open
    turtle.done()

if __name__ == "__main__":
    main()
