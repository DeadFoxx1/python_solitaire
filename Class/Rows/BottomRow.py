from Class.Columns.Column import Column
from Class.Columns.DrawDeck import DrawDeck
from Class.Rows.Row import Row


def set_contents(row, foundation, deck):
    contents = [
        DrawDeck(23, deck),
        Column(-1, deck),
    ]
    contents.extend(Column(0, foundation) for x in range(4))
    return contents


class BottomRow(Row):
    def __init__(
        self, deck: "deck object", num_of_columns, foundation: "foundation deck object"
    ):
        super().__init__(num_of_columns)
        self.contents = set_contents(self, foundation, deck)

    def display(self):
        from setting import get_x_offset, SCREEN_HEIGHT

        x = 0
        for column in self.contents:
            column.display_column(x, SCREEN_HEIGHT)
            x += get_x_offset(self.num_of_columns)

    def draw_card(self):
        # this represents the main drawing deck (furthest to the left)
        main_deck = self.contents[0].contents

        # this represents the column to the right of the main drawing deck (where the cards are drawn to)
        output = self.contents[1].contents

        length_of_deck = len(main_deck)

        if length_of_deck > 3:
            num_cards_to_draw = 3
        else:
            num_cards_to_draw = length_of_deck - 1

        if num_cards_to_draw == 0:
            for card in reversed(output):
                card.is_face_up = False
                main_deck.append(card)
            output.clear()
            return

        for _ in range(num_cards_to_draw):
            drawn_card = main_deck.pop()
            drawn_card.is_face_up = True
            output.append(drawn_card)

    def update_card(self):
        for column in self.contents:
            if len(column.contents) != 0:
                for card in column.contents:
                    card.is_selected = False
                    card.load_image()
