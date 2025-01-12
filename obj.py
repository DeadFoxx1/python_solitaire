import setting
from Class.Deck import Deck
from Class.Column import Column
import pygame


#create deck
deck_main = Deck()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((setting.SCREEN_WIDTH, setting.SCREEN_HEIGHT), pygame.RESIZABLE)

#create 7 rows with asending amts of cards 1-7 (ex: 1-2-3-4-5-6-7). also only the last card is face up
row = []
for ammount in range(7):
    row.append(Column(ammount, deck_main))
    row[ammount].contents[-1].is_face_up = True

draw_deck = Column(23, deck_main)
draw_deck.contents[-1].is_face_up = True