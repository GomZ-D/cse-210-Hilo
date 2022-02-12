import random


class Card:
    """The responsability of cards is to keep track of the points of the cards 
    Attributes:
        points(int): points for guessing card
        num_card (int): number of card
    """
    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.points = 0
        self.num_card= 0

    def deal_card (self):
        """Generates a new random card between 1 and 13.
        
        Args:
            self (Card): An instance of Card.
        """
        pass

    def next_card (self, hilo):
        pass

        
    