from Class.Columns.Column import Column
from Class.Card import Card

class PlayingColumns(Column):
    def set_contents(self):
        self.contents = [self.deck.contents.pop(card) for card in range(self.num_of_cards, -1, -1)]
        self.contents.insert(0, Card(0, 14, True))