import random


class Deck:
    """A deck of cards, all values are between 1 and 13

    The responsibility of Deck is to keep track of the card that's been dealt
   
    Attributes:
        value (int): The number of the card.
    """

    def __init__(self):
        """Constructs a new instance of Deck.

        Args:
            self (Deck): An instance of Decks.
        """
        self.value = 0

    def draw(self):
        """Generates a new random value for the card.
        
        Args:
            self (Deck): An instance of Deck.
        """
        self.value = random.randint(1, 13)
