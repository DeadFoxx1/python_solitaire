from Class.Card import Card
import random

class Deck:
    def __init__(self, foundation: "Optional, bool: if true, will create a deck with only foundation cards" = False):
        self.foundation = foundation
        self.__create_deck()
        
    def __create_deck(self):
        from setting import SUITS
        deck = []
        #create a list of card objects 
        if self.foundation:
            #create list of foundation cards. one for each suit in setting.SUIT
            for suit in SUITS:
                deck.append(Card(suit, 0, True))
        else:
            #create a list of card objects valued 1-13. one for each suit in setting.SUIT
            for suit in SUITS:
                for value in range(1, 14):
                    deck.append(Card(suit, value, False))
            random.shuffle(deck)
        self.contents = deck