from Class.Columns.Foundation import Foundation
from Class.Columns.DrawDeck import DrawDeck
from Class.Columns.DrawnColumn import DrawnColumn
from Class.Rows.Row import Row


def set_contents(row, deck, foundation_deck):
    contents = [
        DrawDeck(24, deck),
        DrawnColumn(),
        # this is used for extra space between foundations and drawn cards
        DrawnColumn(),
    ]
    contents.extend(Foundation(1, foundation_deck) for _ in range(4))
    return contents


class BottomRow(Row):
    def __init__(self, deck: list, num_of_columns: int, foundation_deck: list):
        super().__init__(num_of_columns)
        self.contents = set_contents(self, deck, foundation_deck)

    def display(self):
        from setting import get_card_height, get_screen_width, get_screen_height

        x = 0
        for column in self.contents:
            column.display_column(x, get_screen_height() - get_card_height())
            x += get_screen_width() / 7

    def draw_card(self):
        from setting import CARDS_TO_DRAW

        # this represents the main drawing deck (furthest to the left)
        main_deck = self.contents[0].contents

        # this represents the column to the right of the main drawing deck (where the cards are drawn to)
        output = self.contents[1].contents

        length_of_deck = len(main_deck)

        if length_of_deck > CARDS_TO_DRAW:
            num_cards_to_draw = CARDS_TO_DRAW
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
