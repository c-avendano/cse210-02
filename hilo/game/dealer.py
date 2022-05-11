from game.deck import Deck


class Dealer:
    """A person who directs the game. 
    
    The responsibility of a Dealer is to control the sequence of play.

    Attributes:
        dice (List[Deck]): A list of Deck instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Dealer.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.dice = []
        self.is_playing = True
        self.score = 300
        self.total_score = 300

        for i in range(5):
            Deck = Deck()
            self.dice.append(Deck)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Dealer): An instance of Dealer.
        """
        roll_dice = input("Roll dice? [y/n] ")
        self.is_playing = (roll_dice == "y")
       
    # def do_updates(self):
    #     """Updates the player's score.

    #     Args:
    #         self (Dealer): An instance of Dealer.
    #     """
    #     if not self.is_playing:
    #         return 

    #     for i in range(len(self.dice)):
    #         Deck = self.dice[i]
    #         Deck.roll()
    #         self.score += Deck.points 
    #     self.total_score += self.score


    # def do_outputs(self):
    #     """Displays the dice and the score. Also asks the player if they want to roll again. 

    #     Args:
    #         self (Dealer): An instance of Dealer.
    #     """
    #     if not self.is_playing:
    #         return
        
    #     values = ""
    #     for i in range(len(self.dice)):
    #         Deck = self.dice[i]
    #         values += f"{Deck.value} "

    #     print(f"You rolled: {values}")
    #     print(f"Your score is: {self.total_score}\n")
    #     self.is_playing == (self.score > 0)


    def points(self):
        """This displays the latest card and the score. If score isn't equal to 0, it will ask if user wants to keep playing"""
        points_total=300

        if points_total > 0:
            first_command = input(f"The current points are {points_total}. Want to draw a card? Y/N")
            
            if first_command == "Y":
                #here comes high_or_low, if correct then here we'll add value to points total, if incorrect remove it. Then we loop back to the beggining with the correct point total.
                print("just filling space with this")

            else:
                print("No worries. Game over")
        else:
            print(f"Score is 0 or lower-- Game over!")
