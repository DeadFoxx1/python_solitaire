from Class.Columns.Column import Column
from Class.Card import Card

class DrawDeck(Column):
    def __init__(self, num_of_cards: "int: pass one less then intended amount" , deck: "Deck object"):
        super().__init__(num_of_cards, deck)        

    def select_card(self, pos):
        for card in reversed(self.contents):
            if card.rect.collidepoint(pos):
                print("draw")
                return"draw"

    def __set_contents(self):
        self.contents = [self.deck.contents.pop(card) for card in range(self.num_of_cards, -1, -1)]
        self.contents.insert(0, Card(0, 0, True))