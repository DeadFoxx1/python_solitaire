from Class.Columns.Column import Column
from Class.Columns.DrawDeck import DrawDeck
from Class.Rows.Row import Row

class BottomRow(Row):
    def __init__(self, deck: "deck object", num_of_columns, foundation: "foundation deck object"):
        super().__init__(deck, num_of_columns)
        self.foundation = foundation
        self.__set_contents()

    def __set_contents(self):
        self.contents = [DrawDeck(23, self.deck), Column(-1, self.deck), Column(-1, self.deck)]
        self.contents.extend(Column(0, self.foundation) for x in range(4))

    def display(self):
        from setting import get_x_offset, SCREEN_HEIGHT
        x = 0
        for column in self.contents:
            column.display_column(x, SCREEN_HEIGHT)
            x += get_x_offset(self.num_of_columns)

    def draw_card(self):
        deck = self.contents[0].contents
        output = self.contents[1].contents
        length_of_deck = len(deck)

        if length_of_deck > 3:
            for card in deck[:3]:
                output.append(deck.pop())
            output[-1].is_face_up = True
        elif length_of_deck > 1:
            for card in deck[:(length_of_deck - 1)]:
                output.append(deck.pop())
            output[-1].is_face_up = True
        else:
            end = deck.pop()
            for card in reversed(output):
                deck.append(output.pop())
            deck.insert(0, end)

    def update_card(self):
        for column in self.contents:
            if len(column.contents) != 0:
                for card in column.contents:
                    card.is_selected = False
                    card.load_image()
