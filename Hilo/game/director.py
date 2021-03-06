from game.card import Card
class Director:
    def __init__(self):
        """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (card): A cards instances.
        is_playing (boolean): Whether or not the game is being played.
        total_score (int): The score for the entire game.
        """

        self.is_playing = True
        self.card = Card()
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
        card = self.card.deal_card()
        print(f'The card is: {card}')
        hilo = input("Higher or lower [h\l]: ")
        hilo = hilo.lower()
        other_card=self.card.next_card(hilo)
        print(f'Next card was: {other_card}')


    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        self.total_score = self.total_score + self.card.points
    def do_outputs(self):
        """Display the score and asks the user if he wants to play again. 
        Args:
            self (Director): An instance of Director.
        """
        if self.total_score < 0:
            self.is_playing = False
            print ("Game Over")
            return
        print(f"Your score is: {self.total_score}")
        # print()
        again = input("Play Again? [y/n]: ")
        print()
        again = again.lower()
        if again == "y":
            self.is_playing
        else:
            self.is_playing = False
            print("Thanks! Bye")
        
    
