from game.leaderboard_data import LeaderboardData
from game.leaderboard_ui import LeaderboardUI

class Leaderboard:
    @staticmethod
    def load_leaderboard():
        """Load the leaderboard data."""
        return LeaderboardData.load_leaderboard()

    @staticmethod
    def save_leaderboard(entries):
        """Save the leaderboard data."""
        LeaderboardData.save_leaderboard(entries)

    @staticmethod
    def update_leaderboard(name, score):
        """Update a player's score and save the updated leaderboard."""
        updated_entries = LeaderboardData.update_leaderboard(name, score)
        LeaderboardData.save_leaderboard(updated_entries)

    @staticmethod
    def draw_leaderboard(current_player, current_score):
        """Draw the leaderboard UI, including the current player's status."""
        LeaderboardUI.draw_leaderboard(current_player, current_score)
