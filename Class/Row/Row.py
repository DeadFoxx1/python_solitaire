from Class.Column import Column
from Class.Deck import Deck

class Row:
    def __init__(self, deck: "deck object", num_of_columns):
        if not isinstance(deck, Deck):
            raise ValueError("Must pass in Deck object")
        self.deck = deck
        self.num_of_columns = num_of_columns
        self.set_contents()

    def select_card(self, pos):
        for column in self.contents:
            column.is_selected = False
            for card in column.contents:
                card.is_selected = False
            for card in reversed(column.contents):
                if card.rect.collidepoint(pos):
                    card.is_selected = True
                    column.is_selected = True
                    print(f"card {card.value}{card.suit} selected! {card.is_selected} {column.is_selected}")
                    break
    def update_card(self):
        for column in self.contents:
            for card in column.contents:
                card.load_image()

    def display(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def set_contents(self):
        #will be overridden in subclasses
        raise NotImplementedError("Subclasses should implement this method.")
