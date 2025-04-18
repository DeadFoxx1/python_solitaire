from Class.Columns.Column import Column
from Class.Card import Card


class DrawnColumn(Column):
    def __init__(
        self,
    ):
        super().__init__(-1, [], False)

    def display_column(
        self,
        x,
        y,
    ):
        """iterate through the different cards in the column and displays them on screen with the passed in cords and offset"""
        from setting import CARDS_TO_DRAW, get_screen_width

        for card in self.contents[-max(CARDS_TO_DRAW, 3) :]:
            card.display(x, y)
            x += min(((get_screen_width() / 7) / CARDS_TO_DRAW), 40)

    def select_card(self, pos):
        for card in reversed(self.contents):
            if card.rect.collidepoint(pos) and card == self.contents[-1]:
                card.is_selected = True
                return card
        return
