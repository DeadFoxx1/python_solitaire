from Class.Column import Column
from Class.Deck import Deck

class Row:
    def __init__(self, deck: "deck object", num_of_columns):
        if not isinstance(deck, Deck):
            raise ValueError("Must pass in Deck object")
        self.deck = deck
        self.num_of_columns = num_of_columns
        self.set_contents()
        self.selected_column = None
        self.selected_card = None

    def select_card(self, pos):
        for col in self.contents:
            card = col.select_card(pos)
            if card != None:
                if self.selected_column is None:
                    self.selected_column = col
                    self.selected_card = col.contents.index(card)
                    return 
                else:
                    self.selected_column.move_card(self.selected_card, col)
                    if len(self.selected_column.contents) != 0:
                        self.selected_column.contents[-1].is_face_up = True
                    self.selected_column = None
                    self.selected_card = None
                    card.is_selected = False
                    return
        self.selected_column = None
        self.selected_card = None
               
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
