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
        self.old = 0
        self.new = 0
        self.points = 300
        self.user = ""

    def roll(self):
        """Generates a new random value and calculates the points for the die.
        
        Args:
            self (Die): An instance of Die.
        """
        self.old = random.randint(1, 13)
        self.new = random.randint(1, 13)
        print(self.old)
        self.user = input("Higher or Lower? [h/l]: ")
                
        if self.old < self.new and self.user.lower() == "h" or self.old > self.new and self.user.lower() == "l":
            self.points+=100
            return

        elif self.old > self.new and self.user.lower() == "h" or self.old < self.new and self.user.lower() == "l":
            self.points-=75 
            return

        else: 0