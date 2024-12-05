import turtle

class CardsUI:
    def __init__(self, cards):
        """
        Initialize the CardsUI with a list of card objects.
        :param cards: List of card-like objects (must have `x`, `y`, `is_flipped`, etc.).
        """
        self.cards = cards

    def draw_all_cards(self):
        """
        Draw all cards on the board in their current state (flipped or face-down).
        """
        for card in self.cards:
            card.draw()

    def flip_card(self, x, y):
        """
        Flip a card at the given (x, y) coordinates if clicked.
        :param x: X-coordinate of the click.
        :param y: Y-coordinate of the click.
        :return: The flipped card object if found, None otherwise.
        """
        for card in self.cards:
            if card.is_clicked(x, y) and not card.is_matched:
                card.flip()
                print(f"Card flipped: {card.image}")
                return card
        return None

    def reset_unmatched_cards(self):
        """
        Flip all unmatched cards back to their face-down state and redraw them.
        """
        for card in self.cards:
            if not card.is_matched and card.is_flipped:
                card.flip()
        self.draw_all_cards()  # Refresh the board visually

    def are_all_cards_matched(self):
        """
        Check if all cards have been matched.
        :return: True if all cards are matched, False otherwise.
        """
        return all(card.is_matched for card in self.cards)
