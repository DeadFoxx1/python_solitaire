from Class.Column import Column

class BottomRow:
    def __init__(self, deck, foundation, num_of_collumns):
        self.deck = deck
        self.foundation = foundation
        self.num_of_collumns = num_of_collumns
        self.set_contents()

    def set_contents(self):
        self.contents = [Column(23, self.deck)]
        self.contents[0].contents[-1].is_face_up = True
        self.contents.extend(Column(0, self.foundation) for x in range(4))

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
        from setting import get_x_offset, SCREEN_HEIGHT
        x = 0
        for column in self.contents:
            column.display_column(x, SCREEN_HEIGHT)
            x += get_x_offset(self.num_of_collumns)
