# import random


# class Deck:
#     """A deck of cards, all values are between 1 and 13

#     The responsibility of Deck is to keep track of the card that's been dealt
   
#     Attributes:
#         value (int): The number of the card.
#     """

#     def __init__(self):
#         """Constructs a new instance of Deck.

#         Args:
#             self (Deck): An instance of Decks.
#         """
#         self.value = 0
#         self.points = 0

#     def draw(self):
#         """Generates a new random value for the card.
        
#         Args:
#             self (Deck): An instance of Deck.
#         """
#         self.value = random.randint(1, 14)
#         self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0

import random


class Deck:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
    """

    def __init__(self):
        """Constructs a new instance of Die.

        Args:
            self (Die): An instance of Die.
        """
        self.value = 0
        self.points = 0

    def roll(self):
        """Generates a new random value and calculates the points for the die.
        
        Args:
            self (Die): An instance of Die.
        """
        self.value = random.randint(1, 14)
        self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0