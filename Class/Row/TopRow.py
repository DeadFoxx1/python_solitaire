from Class.Column import Column
from Class.Row.Row import Row

class TopRow(Row):
    def set_contents(self):
        self.contents = [Column(x, self.deck) for x in range(self.num_of_columns)]
        for column in self.contents:
            column.contents[-1].is_face_up = True

    def display(self):
        from setting import get_x_offset, Y_OFFSET
        x = 0
        for column in self.contents:
            column.display_column(x, 0, 0, Y_OFFSET)
            x += get_x_offset(self.num_of_columns)
