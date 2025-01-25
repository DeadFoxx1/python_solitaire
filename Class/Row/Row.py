from Class.Column import Column
from Class.Deck import Deck

class Row:
    def __init__(self, deck: "deck object", num_of_columns):
        if not isinstance(deck, Deck):
            raise ValueError("Must pass in Deck object")
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
            selected_card = column.select_card(pos)
            if selected_card != None:
                return (column, selected_card)
        return

    def move_card(self, column: "destination"):
        if self.card_cache.value == column.contents[-1].value - 1 and self.card_cache.color != column.contents[-1].color:
            self.column_cache.move_card(self.column_cache.contents.index(self.card_cache), column)
            if len(self.column_cache.contents) != 0:
                self.column_cache.contents[-1].is_face_up = True
        self.card_cache.is_selected = False
        self.column_cache = None
        self.card_cache = None
               
    def update_card(self):
        for column in self.contents:
            if len(column.contents) != 0:
                column.contents[-1].is_face_up = True
                for card in column.contents:
                    card.is_selected = False
                    card.load_image()

    def __display(self):
        raise NotImplementedError("overwritten in subclass.")

    def __set_contents(self):
        raise NotImplementedError("overwritten in subclass.")
