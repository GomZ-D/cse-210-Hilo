class Director:
    def __init__(self):
        """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (List[card]): A list of number of cards instances.
        is_playing (boolean): Whether or not the game is being played.
        total_score (int): The score for the entire game.
        """

        self.is_playing = True
        self.card = card()
        self.total_score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while (self.is_playing):
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want a high or low card.

        Args:
            self (Director): An instance of Director.
        """
        pass
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        pass
    def do_outputs(self):
        """Display the score and asks the user if he wants to play again. 
        Args:
            self (Director): An instance of Director.
        """

        pass
    
