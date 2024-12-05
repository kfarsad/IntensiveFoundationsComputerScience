import random

class CardsData:
    @staticmethod
    def generate_card_pairs(card_images, num_cards):
        """
        Generate a shuffled list of card pairs based on the selected number of cards.
        :param card_images: List of card image paths.
        :param num_cards: Number of cards to generate (must be even).
        :return: List of tuples (image_path, id), where each tuple represents a card.
        """
        if num_cards % 2 != 0:
            raise ValueError("Number of cards must be even to form pairs.")

        if len(card_images) < num_cards // 2:
            raise ValueError(
                f"Not enough unique images to generate {num_cards} cards. "
                f"Provide at least {num_cards // 2} unique images."
            )

        # Select the appropriate number of images and duplicate them to create pairs
        selected_images = card_images[:num_cards // 2]
        paired_images = selected_images * 2  # Duplicate images for pairs

        # Shuffle the card pairs
        random.shuffle(paired_images)

        # Return a list of (image_path, unique_id) for each card
        return [(image, i // 2) for i, image in enumerate(paired_images)]
