from Class.Card import Card
import random

class Deck:

    def __init__(self):
        self.contents = self.create_deck()
        

    def create_deck(self):
        from setting import SUITS
        deck = []
        for suit in SUITS:
            for value in range(1, 14):
                deck.append(Card(suit, value, False))
        random.shuffle(deck)
        return deck