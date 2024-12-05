from time import sleep

class GameLogic:
    def __init__(self, board):
        self.board = board
        self.flipped_cards = []
        self.matches = 0
        self.moves = 0

    def flip_card(self, x, y):
        """Handle card flipping logic."""
        for card in self.board.cards:
            if card.x - 50 < x < card.x + 50 and card.y - 75 < y < card.y + 75:
                if not card.is_flipped and not card.is_matched:
                    card.flip()
                    self.board.draw_card(card.image, card.x, card.y)
                    self.flipped_cards.append(card)
                    if len(self.flipped_cards) == 2:
                        self.moves += 1
                        self.check_match()
                return

    def check_match(self):
        """Check if two flipped cards are a match."""
        if self.flipped_cards[0].image == self.flipped_cards[1].image:
            # Cards match
            for card in self.flipped_cards:
                card.is_matched = True
            self.matches += 1
        else:
            # Cards don't match; flip them back after a brief delay
            sleep(1)
            for card in self.flipped_cards:
                card.flip()
                self.board.draw_card('card_back.gif', card.x, card.y)
        self.flipped_cards = []
