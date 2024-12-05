import turtle

class StatusBar:
    @staticmethod
    def draw_status_text(guesses, matches):
        """Display text inside the status bar with guesses and matches."""
        status_text_turtle = turtle.Turtle()
        status_text_turtle.hideturtle()
        status_text_turtle.speed(0)
        status_text_turtle.penup()

        # Position the text lower in the box and align it to the left
        status_text_turtle.goto(-290, -235)  # Adjusted coordinates for left alignment
        status_text_turtle.write(
            f"Status: Guesses: {guesses}, Matches: {matches}",
            align="left",  # Align text to the left
            font=("Arial", 14, "normal")
        )
        return status_text_turtle

    @staticmethod
    def update_status_text(status_text_turtle, guesses, matches):
        """Update text inside the status bar."""
        status_text_turtle.clear()
        status_text_turtle.goto(-290, -235)  # Ensure consistent positioning
        status_text_turtle.write(
            f"Status: Guesses: {guesses}, Matches: {matches}",
            align="left",  # Align text to the left
            font=("Arial", 14, "normal")
        )
