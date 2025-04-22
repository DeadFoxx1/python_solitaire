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
        from setting import CARDS_TO_DRAW, get_screen_width, MAX_DRAWNCARD_X_OFFSET

        for card in self.contents[-max(CARDS_TO_DRAW, 3) :]:
            card.display(x, y)
            # get the space of 2 columns and divide it by the number of cards we plan on displaying. This if the offset we add to each, with a maximum of 40
            x += min(((get_screen_width() / 7) / max(CARDS_TO_DRAW, 3)), MAX_DRAWNCARD_X_OFFSET)

    def select_card(self, pos):
        for card in reversed(self.contents):
            if card.rect.collidepoint(pos) and card == self.contents[-1]:
                card.is_selected = True
                return card
        return
