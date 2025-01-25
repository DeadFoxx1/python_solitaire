from Class.Column import Column
from Class.Row.Row import Row

class BottomRow(Row):
    def __init__(self, deck: "deck object", num_of_columns, foundation: "foundation deck object"):
        super().__init__(deck, num_of_columns)
        self.foundation = foundation
        self.__set_contents()

    def __set_contents(self):
        self.contents = [Column(23, self.deck)]
        self.contents.extend(Column(0, self.foundation) for x in range(4))

    def display(self):
        from setting import get_x_offset, SCREEN_HEIGHT
        x = 0
        for column in self.contents:
            column.display_column(x, SCREEN_HEIGHT)
            x += get_x_offset(self.num_of_columns)
