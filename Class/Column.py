from Class.Deck import Deck

class Column:
    def __init__(self, num_of_cards: "int: pass one less then intended amount" , deck: "Deck object"):
        if not isinstance(deck, Deck):
            raise ValueError("Must pass in Deck object")

        self.deck = deck
        self.num_of_cards = num_of_cards
        self.__set_contents()
    #takes however many cards specified in num_of_cards from the passed in Deck and removes it from the Deck    
    def __set_contents(self):
        self.contents = [self.deck.contents.pop(card) for card in range(self.num_of_cards, -1, -1)]

    @property
    def num_of_cards(self):
        return self.__num_of_cards

    @num_of_cards.setter
    def num_of_cards(self, num_of_cards):
        if num_of_cards <= len(self.deck.contents) - 1:
            self.__num_of_cards = num_of_cards
        else:
            raise IndexError(f"deck {deck} does not have enough cards ({num_of_cards}) to create column")

    def display_column(self, x, y, x_offset: "Optional, int: adds this value to x after every card" = 0, y_offset: "Optional, int: adds this value to y after every card" = 0):
        """iterate through the different cards in the column and displays them on screen with the passed in cords and offset"""
        for card in self.contents:
            card.display(x, y)
            x += x_offset
            y += y_offset

    def select_card(self, pos):
        for card in reversed(self.contents):
            if card.rect.collidepoint(pos):
                card.is_selected = True
                return card
        return


    def move_card(self, card_index, column):
        for card in range(card_index, len(self.contents)):
            column.contents.append(self.contents.pop(card_index))