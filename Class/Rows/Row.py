from Class.Columns.Column import Column
from Class.Deck import Deck


class Row:
    def __init__(self, deck: "deck object", num_of_columns):
        if not isinstance(deck, Deck):
            raise ValueError("Must pass a Deck object")
        self.deck = deck
        self.num_of_columns = num_of_columns
        self.set_cache = None

    def clear_select_cards(self):
        for column in self.contents:
            for card in column.contents:
                card.is_selected = False

    def select_card(self, pos):
        self.clear_select_cards()
        for column in self.contents:
            if (result := column.select_card(pos)) == "draw":
                return "draw"
            elif result != None:
                return (column, result)
        return

    def __update_card(self):
        raise NotImplementedError("overwritten in subclass.")

    def __display(self):
        raise NotImplementedError("overwritten in subclass.")

    def __set_contents(self):
        raise NotImplementedError("overwritten in subclass.")
