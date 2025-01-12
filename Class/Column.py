from Class.Deck import Deck

class Column:

    def __init__(self, num_of_cards: int, deck: "Deck object"):
        if not isinstance(deck, Deck):
            raise ValueError("Must pass in Deck object")
        
        self.num_of_cards = num_of_cards
        self.contents = self.create_column(deck)
        
    def create_column(self, deck):
        contents = []
        for card in range(self.num_of_cards, -1, -1):
            contents.append(deck.contents[card])
            deck.contents.pop(card)
        return contents

    def display_column(self, x, y,x_offset: "optional" = 0, y_offset: "optional" = 0):
        from obj import screen
        for card in self.contents:
            screen.blit(card.image, (x, y))
            x += x_offset
            y += y_offset