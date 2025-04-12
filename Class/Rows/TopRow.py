from Class.Columns.PlayingColumn import PlayingColumn
from Class.Rows.Row import Row


class TopRow(Row):

    def __init__(self, deck: "list", num_of_columns):
        super().__init__(num_of_columns)
        self.contents = [
            PlayingColumn(x + 1, deck, True) for x in range(self.num_of_columns)
        ]

    def display(self):
        from setting import get_x_offset, Y_OFFSET

        x = 0
        for column in self.contents:
            column.display_column(x, 0, Y_OFFSET)
            x += get_x_offset(self.num_of_columns)

    def update_card(self):
        super().update_card()
        for column in self.contents:
            if column.contents:
                column.contents[-1].is_face_up = True
