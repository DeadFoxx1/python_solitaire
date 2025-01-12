from Deck import Deck
from Column import Column

#create deck
deck_main = Deck()

#create 7 rows with asending amts of cards 1-7 (ex: 1-2-3-4-5-6-7). also only the last card is face up
row = []
for ammount in range(8):
    row.append(Column(ammount + 1, deck_main))
    row[ammount].contents[-1].is_face_up = True