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
        self.num_card =  random.randint(1,13)
        return self.num_card

    def next_card (self, hilo):
        """ gives another card and calculate the score
        Args:
            Self (Card): an instance of Card
            hilo (string): Answer of user if he wants Hi or Low
        """
        other_card = self.num_card

        while (other_card == self.num_card):
            other_card = random.randint(1,13)

        if other_card < self.num_card:
            answer = 'l'
        else:
            answer = 'h'
        
        if answer == hilo:
            self.points = 100
        else:
            self.points = -75
        return other_card



        
    