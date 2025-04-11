from Class.Columns.Column import Column
from Class.Card import Card


class Foundation(Column):
    def __init__(
        self,
        num_of_cards: "int: pass one less then intended amount",
        deck: "list",
    ):
        super().__init__(num_of_cards, deck, False)
