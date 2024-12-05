import turtle
from game.leaderboard_data import LeaderboardData

class LeaderboardUI:
    # Create a single instance of Turtle for the leaderboard
    _leaderboard_turtle = None

    @staticmethod
    def _get_leaderboard_turtle():
        """
        Return a single instance of the leaderboard Turtle.
        """
        if LeaderboardUI._leaderboard_turtle is None:
            LeaderboardUI._leaderboard_turtle = turtle.Turtle()
            LeaderboardUI._leaderboard_turtle.hideturtle()
            LeaderboardUI._leaderboard_turtle.speed(0)
        return LeaderboardUI._leaderboard_turtle

    @staticmethod
    def draw_leaderboard(current_player, current_score):
        """
        Dynamically position leaders and the current player based on scores.
        Clears and redraws the leaderboard to ensure no text overlaps.
        """
        # Load leaderboard and add the current player
        entries = LeaderboardData.load_leaderboard()
        entries_with_current = entries + [(current_score, current_player)]

        # Sort for real-time ranking
        entries_with_current = sorted(entries_with_current, key=lambda x: x[0])

        # Get the shared Turtle instance
        leaderboard_turtle = LeaderboardUI._get_leaderboard_turtle()

        # Clear previous text
        leaderboard_turtle.clear()

        # Draw leaderboard
        leaderboard_turtle.penup()
        leaderboard_turtle.goto(170, 230)
        leaderboard_turtle.color("blue")
        leaderboard_turtle.write("Leaders:", align="left", font=("Arial", 14, "bold"))

        # Draw each leaderboard entry (limit to 10 for space)
        y_offset = 210
        for rank, (score, name) in enumerate(entries_with_current[:10], start=1):
            leaderboard_turtle.goto(170, y_offset)
            if name == current_player:
                leaderboard_turtle.color("red")  # Highlight current player
            else:
                leaderboard_turtle.color("blue")
            leaderboard_turtle.write(f"{rank}. {name}: {score}", align="left", font=("Arial", 12, "normal"))
            y_offset -= 30
