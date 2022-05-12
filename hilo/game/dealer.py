from game.deck import Deck


class Dealer:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[deck]): A list of deck instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.deck = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        
        
        for i in range(1):
            deck = Deck()
            self.deck.append(deck)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            
            self.do_updates()
            self.do_outputs()
            self.get_inputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        if self.total_score <= 0:
            self.is_playing = False
            print('GAME OVER')

        else: 
            play_again = input("Play again? [y/n]: ")
            self.is_playing = (play_again == "y")
            if not self.is_playing:
                print()
                print('Thanks for playing')

            print()


    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        for i in range(len(self.deck)):
            deck = self.deck[i]
            deck.roll()
            self.score = deck.points 
        self.total_score = self.score        

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            print("GAME OVER!")
            return
        
        values = ""
        for i in range(len(self.deck)):
            deck = self.deck[i]
            values += f"{deck.new} "

        print(f"Next cart was: {values}")
        print(f"Your score is: {self.total_score}")
        self.is_playing == (self.score > 0)

