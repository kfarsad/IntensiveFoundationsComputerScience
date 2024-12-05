class BoardData:
    @staticmethod
    def calculate_card_positions(rows, cols, card_width, card_height):
        """
        Calculate the x, y positions for each card on the board.
        :param rows: Number of rows on the board.
        :param cols: Number of columns on the board.
        :param card_width: Width of each card.
        :param card_height: Height of each card.
        :return: List of tuples (x, y) for each card position.
        """
        positions = []
        for row in range(rows):
            for col in range(cols):
                x = col * card_width - (cols * card_width) // 2 + card_width // 2
                y = (rows * card_height) // 2 - row * card_height - card_height // 2
                positions.append((x, y))
        return positions

    @staticmethod
    def is_valid_board(rows, cols, num_cards):
        """
        Validate if the board can accommodate the number of cards.
        :param rows: Number of rows.
        :param cols: Number of columns.
        :param num_cards: Total number of cards.
        :return: True if the configuration is valid, False otherwise.
        """
        return rows * cols >= num_cards
