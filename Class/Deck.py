from Class.Card import Card
import random

class Deck:

    def __init__(self):
        self.contents = self.create_deck()
        

    def create_deck(self):
        deck = []
        suits = ["h", "s", "c", "d"]
        for suit in suits:
            for value in range(13):
                deck.append(Card(suit, value, False))
        random.shuffle(deck)
        return deck