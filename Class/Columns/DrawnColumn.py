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
        for card in self.contents[-3:]:
            card.display(x, y)
            x += 20
