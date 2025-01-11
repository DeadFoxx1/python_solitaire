from Deck import Deck
from Column import Column

deck_main = Deck()
column1 = Column(7, deck_main)

for card in column1.contents:
    print(str(card.suit))