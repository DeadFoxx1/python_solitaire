from Class.Column import Column

class TopRow:
    def __init__(self, deck, num_of_collumns):
        self.deck = deck
        self.num_of_collumns = num_of_collumns
        self.set_contents()

    def set_contents(self):
        self.contents = [Column(x, self.deck) for x in range(self.num_of_collumns)]
        for column in self.contents:
            column.contents[-1].is_face_up = True

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
        from setting import get_x_offset, Y_OFFSET
        x = 0
        for column in self.contents:
            column.display_column(x, 0, 0, Y_OFFSET)
            x += get_x_offset(self.num_of_collumns)
