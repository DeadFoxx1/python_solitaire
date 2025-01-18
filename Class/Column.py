from Class.Deck import Deck

class Column:

    def __init__(self, num_of_cards: "int: pass one less then intended amount" , deck: "Deck object"):
        if not isinstance(deck, Deck):
            raise ValueError("Must pass in Deck object")

        self.__set_num_of_cards(num_of_cards, deck)
        #takes however many cards specified in num_of_cards from the passed in Deck and removes it from the Deck
        self.contents = [deck.contents.pop(card) for card in range(self.num_of_cards, -1, -1)]
    
    @property
    def num_of_cards(self):
        return self.__num_of_cards

    def __set_num_of_cards(self, num_of_cards, deck):
        if num_of_cards <= len(deck.contents) - 1:
            self.__num_of_cards = num_of_cards
        else:
            raise IndexError(f"deck {deck} does not have enough cards ({num_of_cards}) to create column")

    #iterate through the different cards in the column and displays them on screen with the passed in cords and offset
    def display_column(self, x, y, x_offset: "Optional, int: adds this value to x after every card" = 0, y_offset: "Optional, int: adds this value to y after every card" = 0):
        from obj import screen
        for card in self.contents:
            screen.blit(card.image, (x, y))
            card.rect = (x, y)
            x += x_offset
            y += y_offset