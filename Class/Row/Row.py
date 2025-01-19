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
        for column in self.contents:
            for card in column.contents:
                card.is_selected = False

        for column in self.contents:
            for card in reversed(column.contents):
                if card.rect.collidepoint(pos):
                    if self.selected_column is None:
                        self.selected_column = column
                        card.is_selected = True
                        self.selected_card = card
                    else:
                        self.selected_column.move_card(self.selected_column.contents.index(self.selected_card), column)
                        if len(self.selected_column.contents) != 0:
                            self.selected_column.contents[-1].is_face_up = True
                        self.selected_column = None
                        self.selected_card.is_selected = False
                        self.selected_card = None
                    print(f"card {card.value}{card.suit} selected! {card.is_selected}")
                    break
                    
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
