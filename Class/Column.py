from Class.Deck import Deck

class Column:
    def __init__(self, num_of_cards: "int: pass one less then intended amount" , deck: "Deck object"):
        if not isinstance(deck, Deck):
            raise ValueError("Must pass in Deck object")

        self.deck = deck
        self.num_of_cards = num_of_cards
        #takes however many cards specified in num_of_cards from the passed in Deck and removes it from the Deck
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

    #iterate through the different cards in the column and displays them on screen with the passed in cords and offset
    def display_column(self, x, y, x_offset: "Optional, int: adds this value to x after every card" = 0, y_offset: "Optional, int: adds this value to y after every card" = 0):
        from obj import screen
        for card in self.contents:
            if card.is_selected:
                card.yellow_highlight.set_alpha(128)
            else:
                card.yellow_highlight.set_alpha(0)
            screen.blit(card.image, (x, y))
            screen.blit(card.yellow_highlight, (x, y))
            card.rect.topleft = (x, y)
            x += x_offset
            y += y_offset