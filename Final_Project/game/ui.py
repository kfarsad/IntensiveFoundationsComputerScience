import turtle
from game.layout import Layout
from game.status_bar import StatusBar
from game.leaderboard import Leaderboard
from game.quit_handler import QuitHandler

class UI:
    @staticmethod
    def initialize_screen(title, width, height):
        """Initialize the Turtle screen."""
        screen = turtle.Screen()
        screen.title(title)
        screen.setup(width=width, height=height)
        screen.bgcolor("white")
        return screen

    @staticmethod
    def draw_layout():
        """Draw the static layout for the game before cards load."""
        Layout.draw_layout()

    @staticmethod
    def draw_status_bar_text(guesses, matches):
        """Display text inside the status bar with guesses and matches."""
        return StatusBar.draw_status_text(guesses, matches)

    @staticmethod
    def update_status_bar_text(status_text_turtle, guesses, matches):
        """Update text inside the status bar."""
        StatusBar.update_status_text(status_text_turtle, guesses, matches)

    @staticmethod
    def load_leaderboard():
        """Load the leaderboard from a file."""
        return Leaderboard.load_leaderboard()

    @staticmethod
    def save_leaderboard(entries):
        """Save the leaderboard to a file."""
        Leaderboard.save_leaderboard(entries)

    @staticmethod
    def draw_leaderboard(entries):
        """Draw the leaderboard inside the leaderboard box."""
        return Leaderboard.draw_leaderboard(entries)
    
    @staticmethod
    def bind_quit_button(screen):
        """Bind the quit button to the 'q' key."""
        QuitHandler.bind_quit_button(screen)

    @staticmethod
    def bind_quit_click():
        """Bind the quit functionality to a mouse click."""
        QuitHandler.bind_quit_click()

