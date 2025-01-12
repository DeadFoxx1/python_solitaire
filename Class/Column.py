from Class.Deck import Deck

class Column:

    def __init__(self, num_of_cards: int, deck: "Deck object"):
        if not isinstance(deck, Deck):
            raise ValueError("Must pass in Deck object")
        
        self.num_of_cards = num_of_cards
        self.contents = self.create_column(deck)
        
    def create_column(self, deck):
        contents = []
        for card in range(self.num_of_cards):
            contents.append(deck.contents[card])
            deck.contents.pop(card)
        return contents