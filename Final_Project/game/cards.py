from game.cards_data import CardsData
from game.cards_ui import CardsUI
from game.card import Card

class CardManager:
    def __init__(self, card_images, num_cards, rows, cols, card_back_image, card_width=100, card_height=150):
        """
        Initialize the CardManager to handle cards and their interactions.
        :param card_images: List of card image paths.
        :param num_cards: Number of cards to play with.
        :param rows: Number of rows on the board.
        :param cols: Number of columns on the board.
        :param card_back_image: Path to the back image for all cards.
        :param card_width: Width of each card.
        :param card_height: Height of each card.
        """
        if rows * cols < num_cards:
            raise ValueError("The board dimensions cannot accommodate the number of cards.")

        self.rows = rows
        self.cols = cols
        self.card_width = card_width
        self.card_height = card_height
        self.cards = []
        self.cards_ui = None
        self.generate_cards(card_images, num_cards, card_back_image)

    def generate_cards(self, card_images, num_cards, card_back_image):
        """
        Generate cards, assign positions, and initialize the CardsUI.
        :param card_images: List of card image paths.
        :param num_cards: Number of cards to generate.
        :param card_back_image: Path to the back image for all cards.
        """
        try:
            # Generate shuffled card pairs and positions
            card_pairs = CardsData.generate_card_pairs(card_images, num_cards)
            positions = CardsData.calculate_card_positions(self.rows, self.cols, self.card_width, self.card_height)

            # Create Card objects and set their back image
            self.cards = [
                Card(image, x, y, card_id) for (image, card_id), (x, y) in zip(card_pairs, positions)
            ]
            for card in self.cards:
                card.set_back_image(card_back_image)

            # Initialize CardsUI with the generated cards
            self.cards_ui = CardsUI(self.cards)

        except Exception as e:
            raise RuntimeError(f"Error generating cards: {e}")

    def draw_all_cards(self):
        """Draw all cards on the board."""
        self.cards_ui.draw_all_cards()

    def flip_card(self, x, y):
        """
        Flip a card at the given (x, y) position.
        :param x: X-coordinate of the click.
        :param y: Y-coordinate of the click.
        :return: The flipped Card object if found, None otherwise.
        """
        flipped_card = self.cards_ui.flip_card(x, y)
        if flipped_card:
            print(f"Card flipped: {flipped_card.image}")
        return flipped_card

    def reset_unmatched_cards(self):
        """Flip all unmatched cards back to their face-down state."""
        print("Resetting unmatched cards...")
        self.cards_ui.reset_unmatched_cards()

    def are_all_cards_matched(self):
        """
        Check if all cards are matched.
        :return: True if all cards are matched, False otherwise.
        """
        all_matched = self.cards_ui.are_all_cards_matched()
        if all_matched:
            print("All cards matched!")
        return all_matched
