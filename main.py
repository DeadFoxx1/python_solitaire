from Deck import Deck
from Column import Column

deck_main = Deck()
row = []
for ammount in range(8):
    row.append(Column(ammount + 1, deck_main))

# for column in row:
#     print("\n")
#     for card in column.contents:
#         print(str(card.value) + str(card.suit))

# for card in deck_main.contents:
#     print(str(card.value) + str(card.suit))