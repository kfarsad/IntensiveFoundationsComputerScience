from game.board_data import BoardData
from game.board_ui import BoardUI
from game.cards import Card
from game.cards_data import CardsData

class Board:
    def __init__(self, rows, cols, card_images):
        """
        Initialize the board.
        :param rows: Number of rows on the board.
        :param cols: Number of columns on the board.
        :param card_images: List of card image paths.
        """
        self.rows = rows
        self.cols = cols
        self.card_images = card_images
        self.card_width = 100
        self.card_height = 150
        self.cards = []
        self.board_ui = BoardUI(rows, cols, self.card_width, self.card_height)

    def initialize_board(self):
        """
        Initialize the board by creating card objects and positioning them.
        """
        if not BoardData.is_valid_board(self.rows, self.cols, len(self.card_images)):
            raise ValueError("Invalid board configuration: Too many cards for the board dimensions.")

        positions = BoardData.calculate_card_positions(self.rows, self.cols, self.card_width, self.card_height)
        card_pairs = CardsData.generate_card_pairs(self.card_images, len(positions))

        for position, image in zip(positions, card_pairs):
            x, y = position
            self.cards.append(Card(image, x, y))

    def draw(self):
        """
        Draw the board grid and all cards in their initial face-down state.
        """
        self.board_ui.draw_board_grid()
        for card in self.cards:
            card.draw()
