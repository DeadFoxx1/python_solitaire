from Class.Column import Column
from Class.Deck import Deck

class Row:
    def __init__(self, deck: "deck object", num_of_columns):
        if not isinstance(deck, Deck):
            raise ValueError("Must pass in Deck object")
        self.deck = deck
        self.num_of_columns = num_of_columns
        self.set_contents()
        self.column_cache = None
        self.card_cache = None

    def select_card(self, pos):
        for column in self.contents:
            selected_card = column.select_card(pos)
            if selected_card is None:
                continue
            if self.column_cache is None:
                self.column_cache = column
                self.card_cache = selected_card
                return 
            else:
                selected_card.is_selected = False
                self.move_card(column)
                return
        self.column_cache = None
        self.card_cache = None

    def move_card(self, column: "destination"):
        if self.card_cache.value == column.contents[-1].value - 1:
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

    def display(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def set_contents(self):
        #will be overridden in subclasses
        raise NotImplementedError("Subclasses should implement this method.")
