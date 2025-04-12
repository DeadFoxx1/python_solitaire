from Class.Columns.Column import Column
from Class.Card import Card


class PlayingColumn(Column):
    def __init__(
        self,
        num_of_cards: int,
        deck: list,
        can_accept_cards: bool,
    ):
        super().__init__(num_of_cards, deck, can_accept_cards)
        self.contents.insert(0, Card(0, 14, True))

    def display_column(
        self,
        x,
        y,
        y_offset: "int" = 0,
    ):
        """iterate through the different cards in the column and displays them on screen with the passed in cords and offset"""
        for card in self.contents:
            card.display(x, y)
            y += y_offset
