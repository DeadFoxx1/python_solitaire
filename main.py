from Deck import Deck
from Column import Column

deck_main = Deck()
row = []
for ammount in range(8):
    row.append(Column(ammount + 1, deck_main))
    row[ammount].contents[-1].is_face_up = True

#debug
# for column in row:
#     print("\n")
#     for card in column.contents:
#         print(str(card.value) + str(card.suit) + str(card.is_face_up))

# for card in deck_main.contents:
#     print(str(card.value) + str(card.suit) + str(card.is_face_up))