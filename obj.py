import pygame
from setting import SCREEN_WIDTH, SCREEN_HEIGHT
from Class.Deck import Deck
from Class.Column import Column


#create necessary pygame objects for screen and fps controll
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

#create deck
deck_main = Deck()
#create second deck with just foundation cards
foundation = Deck(True)

#create 7 columns with asending amts of cards 1-7 (ex: 1-2-3-4-5-6-7).
top_row = [Column(ammount, deck_main) for ammount in range(7)]
#loop to face last card in each column up
for column in top_row:
    column.contents[-1].is_face_up = True

#create bottom row with draw deck (remainder of cards in deck_main) and foundations
bottom_row = [Column(23, deck_main)]
#turn last card in draw deck face up
bottom_row[0].contents[-1].is_face_up = True
#add the foundations to bottom row
bottom_row.extend(Column(0, foundation) for x in range(4))

