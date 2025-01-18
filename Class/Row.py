from Class.Column import Column

class Row:
    def __init__(self, deck, num_of_columns):
        self.deck = deck
        self.num_of_columns = num_of_columns
        self.contents = []
        self.set_contents()

    def set_contents(self):
        #will be overridden in subclasses
        raise NotImplementedError("Subclasses should implement this method.")

    def select_card(self, pos):
        for column in self.contents:
            for card in reversed(column.contents):
                if card.rect.collidepoint(pos):
                    print(f"card {card.value}{card.suit} selected!")
                    break

    def update_card(self):
        for column in self.contents:
            for card in column.contents:
                card.load_image()

    def display(self):
        from setting import get_x_offset
        x = 0
        for column in self.contents:
            column.display_column(x, 0)  # Default y position can be overridden
            x += get_x_offset(self.num_of_columns)
