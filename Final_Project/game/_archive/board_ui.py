import turtle

class BoardUI:
    def __init__(self, rows, cols, card_width=100, card_height=150):
        """
        Initialize the BoardUI.
        :param rows: Number of rows on the board.
        :param cols: Number of columns on the board.
        :param card_width: Width of each card.
        :param card_height: Height of each card.
        """
        self.rows = rows
        self.cols = cols
        self.card_width = card_width
        self.card_height = card_height

    def draw_board_grid(self):
        """
        Draw the grid for the board layout.
        """
        turtle.penup()
        turtle.speed(0)
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.card_width - (self.cols * self.card_width) // 2
                y = (self.rows * self.card_height) // 2 - row * self.card_height
                turtle.goto(x, y)
                turtle.pendown()
                for _ in range(2):
                    turtle.forward(self.card_width)
                    turtle.right(90)
                    turtle.forward(self.card_height)
                    turtle.right(90)
                turtle.penup()
