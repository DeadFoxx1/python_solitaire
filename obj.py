import pygame
from setting import SCREEN_WIDTH, SCREEN_HEIGHT
from Class.Deck import Deck
from Class.Column import Column
from Class.Row.TopRow import TopRow
from Class.Row.BottomRow import BottomRow

#create necessary pygame objects for screen and fps control
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

#create deck
deck_main = Deck()

#create second deck with just foundation cards
foundation = Deck(True)

#create 7 columns with ascending amounts of cards 1-7 (ex: 1-2-3-4-5-6-7).
top_row = TopRow(deck_main, 7)

#create bottom row with draw deck (remainder of cards in deck_main) and foundations
bottom_row = BottomRow(deck_main, 7, foundation)