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
        from setting import MAX_Y_OFFSET, get_card_height, get_screen_height

        for card in self.contents:
            card.display(x, y)
            y += min(
                MAX_Y_OFFSET,
                # basically divide the height above the bottom row by how many cards that are in the collumn
                # and if negative, use 0
                max(
                    0,
                    (get_screen_height() - (2 * get_card_height()))
                    / len(self.contents),
                ),
            )
