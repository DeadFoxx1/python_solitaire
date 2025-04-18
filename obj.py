import pygame, random
from setting import SUITS
from Class.Rows.TopRow import TopRow
from Class.Rows.BottomRow import BottomRow
from Class.Card import Card


def create_shuffled_deck():
    deck = [Card(suit, value, False) for value in range(1, 14) for suit in SUITS]
    random.shuffle(deck)
    return deck


clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

deck = create_shuffled_deck()

foundation_deck = [Card(suit, 0, True) for suit in SUITS]

bottom_row = BottomRow(deck, 7, foundation_deck)

top_row = TopRow(deck, 7)
