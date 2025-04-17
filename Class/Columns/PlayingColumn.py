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
    ):
        """iterate through the different cards in the column and displays them on screen with the passed in cords and offset"""
        from setting import Y_OFFSET, SCREEN_HEIGHT, CARD_HEIGHT

        for card in self.contents:
            card.display(x, y)
            y += min(
                Y_OFFSET,
                (SCREEN_HEIGHT - len(self.contents)) / len(self.contents)
            )
