import random


class Deck:
    """A Deck of cards from 1 to 13. This class will bring up a number at random.
   
    Attributes:
        old (int): The number the previous card.
        new (int): The number of the current card.
    """

    def __init__(self):
        """Constructs a new instance of Die.

        Args:
        old (int): The number the previous card.
        new (int): The number of the current card.
        """
        self.old = 0
        self.new = 0
        self.points = 300
        self.user = ""

    def roll(self):
        """Rolls a new random value, compares it with the old one and calculates the points you get from the card.
        
        Args:
        old (int): The number the previous card.
        new (int): The number of the current card.
            
        """
        self.old = random.randint(1, 13)
        self.new = random.randint(1, 13)
        print(f'The card is: {self.old}')
        self.user = input("Higher or Lower? [h/l]: ")
                
        if self.old < self.new and self.user.lower() == "h" or self.old > self.new and self.user.lower() == "l":
            self.points+=100
            return

        elif self.old > self.new and self.user.lower() == "h" or self.old < self.new and self.user.lower() == "l":
            self.points-= 75 
            return

        else: 0
