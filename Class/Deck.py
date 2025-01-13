from Class.Card import Card
import random

class Deck:

    def __init__(self, foundation: "optional" = False):
        self.foundation = foundation
        self.contents = self.create_deck()
        

    def create_deck(self):
        from setting import SUITS
        deck = []
        if self.foundation:
            for suit in SUITS:
                deck.append(Card(suit, 0, True, True))
        else:
            for suit in SUITS:
                for value in range(1, 14):
                    deck.append(Card(suit, value, False, False))
            random.shuffle(deck)
        return deck