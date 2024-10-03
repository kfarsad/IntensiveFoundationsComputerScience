'''
    CS 5001 Lab 2
    Fall 2020
    my_squareStretch.py
    Note: errors occuring due to not having copy of image to use for stretch goal.
'''

import turtle

# Constants for square and window setup
SQUARE_LENGTH = 80
RADIUS = SQUARE_LENGTH / 2
WIDTH = 970
HEIGHT = 635

def setup():
    '''
    Function: setup
    Parameters: None
    Returns: Nothing
    Does: sets up the environment so we can display the background picture
    '''
    turtle.hideturtle()
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)

    # Update the path to the correct file location on your device
    turtle.bgpic('/Users/keavanfarsad/My Drive/Northeastern University/2024_09_04 CS5001 - Intensive Foundations in Computer Science/Lab/Lab2/shape_window.gif')
    
    turtle.penup()

def draw_square(pen, length):
    ''' Helper function to draw a square '''
    pen.down()
    for _ in range(4):
        pen.forward(length)
        pen.right(90)
    pen.up()

def draw_circle(pen, radius):
    ''' Helper function to draw an inscribed circle '''
    pen.down()
    pen.circle(radius)
    pen.up()

def move_shapes(new_x_square, new_y_square, new_x_circle, new_y_circle):
    ''' Function to move shapes based on user input '''
    pen = turtle.Turtle()
    pen.hideturtle()

    # Clear previous drawing
    turtle.clear()

    # Move to new square coordinates and draw the square
    pen.goto(new_x_square - SQUARE_LENGTH / 2, new_y_square + SQUARE_LENGTH / 2)
    pen.pencolor("blue")
    pen.fillcolor("blue")
    pen.begin_fill()
    draw_square(pen, SQUARE_LENGTH)
    pen.end_fill()

    # Move to new circle coordinates and draw the circle
    pen.goto(new_x_circle, new_y_circle - RADIUS)
    pen.pencolor("magenta")
    pen.fillcolor("magenta")
    pen.begin_fill()
    draw_circle(pen, RADIUS)
    pen.end_fill()

def draw_initial_shapes():
    ''' Draw initial shapes at (0, 0) '''
    pen = turtle.Turtle()
    pen.hideturtle()

    # Draw the initial square at the center (0, 0)
    pen.goto(-SQUARE_LENGTH / 2, SQUARE_LENGTH / 2)
    pen.pencolor("blue")
    pen.fillcolor("blue")
    pen.begin_fill()
    draw_square(pen, SQUARE_LENGTH)
    pen.end_fill()

    # Draw the inscribed circle in the square
    pen.goto(0, -RADIUS)
    pen.pencolor("magenta")
    pen.fillcolor("magenta")
    pen.begin_fill()
    draw_circle(pen, RADIUS)
    pen.end_fill()

def main():
    setup()  # Set up the environment with the background
    draw_initial_shapes()  # Draw the initial square and circle at (0, 0)

    # Prompt the user for new (x, y) coordinates
    new_x_square = int(input("Enter the new x-coordinate for the square: "))
    new_y_square = int(input("Enter the new y-coordinate for the square: "))
    new_x_circle = int(input("Enter the new x-coordinate for the circle: "))
    new_y_circle = int(input("Enter the new y-coordinate for the circle: "))

    # Move the shapes to new coordinates
    move_shapes(new_x_square, new_y_square, new_x_circle, new_y_circle)

    # Keep the turtle window open
    turtle.done()

if __name__ == "__main__":
    main()
