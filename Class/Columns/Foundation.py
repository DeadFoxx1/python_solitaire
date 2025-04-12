from Class.Columns.Column import Column


class Foundation(Column):
    def __init__(
        self,
        num_of_cards: int,
        deck: list,
    ):
        super().__init__(num_of_cards, deck, False)
