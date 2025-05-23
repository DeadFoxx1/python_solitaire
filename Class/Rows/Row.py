class Row:
    def __init__(self, num_of_columns):
        self.num_of_columns = num_of_columns
        self.set_cache = None

    def clear_select_cards(self):
        for column in self.contents:
            for card in column.contents:
                card.is_selected = False

    def select_card(self, pos):
        self.clear_select_cards()
        for column in self.contents:
            if (selected_card := column.select_card(pos)) == "draw":
                return "draw"
            elif selected_card != None:
                return (column, selected_card)
        return

    def update_card(self):
        for column in self.contents:
            if column.contents:
                for card in column.contents:
                    card.is_selected = False
                    card.load_image()
