import turtle
import os

class Layout:
    @staticmethod
    def draw_rectangle(turtle_obj, x, y, width, height, color=None, fill=False, pensize=5):
        """Utility function to draw a rectangle with customizable lines."""
        turtle_obj.penup()
        turtle_obj.goto(x, y)
        turtle_obj.pendown()
        turtle_obj.pensize(pensize)  # Set line thickness
        if color:
            turtle_obj.color(color)
        if fill:
            turtle_obj.begin_fill()
        for _ in range(2):
            turtle_obj.forward(width)
            turtle_obj.right(90)
            turtle_obj.forward(height)
            turtle_obj.right(90)
        if fill:
            turtle_obj.end_fill()

    @staticmethod
    def draw_layout():
        """Draw the static layout for the game before cards load."""
        layout_turtle = turtle.Turtle()
        layout_turtle.speed(3)  # Moderate speed to visualize the drawing
        layout_turtle.shape("classic")  # Use the default turtle pointer
        layout_turtle.showturtle()

        # Draw the game board area
        Layout.draw_rectangle(layout_turtle, -300, 250, 400, 400, color="black", pensize=5)

        # Draw the status bar area
        Layout.draw_rectangle(layout_turtle, -300, -200, 400, 50, color="black", pensize=5)

        # Draw the leaderboard area
        Layout.draw_rectangle(layout_turtle, 150, 250, 200, 400, color="blue", pensize=5)

        # Hide the turtle after drawing is complete
        layout_turtle.hideturtle()

    @staticmethod
    def add_quit_button(asset_path):
        """Add the quit button using an asset."""
        # Load the quit button asset
        quit_turtle = turtle.Turtle()
        quit_turtle.speed(0)
        quit_turtle.penup()
        quit_turtle.goto(200, -225)  # Center the button where the rectangle is drawn
        quit_turtle.shape(asset_path)
        quit_turtle.showturtle()
        return quit_turtle

    @staticmethod
    def add_quit_button(asset_path):
        """Add the quit button using the provided asset."""
        quit_turtle = turtle.Turtle()
        quit_turtle.speed(0)
        quit_turtle.penup()
        quit_turtle.goto(200, -225)  # Center the button where the rectangle was drawn
        quit_turtle.shape(asset_path)
        quit_turtle.showturtle()
        return quit_turtle