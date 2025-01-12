#contaiins utilities used in game
import pygame


def game_init():
    from obj import row, deck_main
    #init pygame
    pygame.init()

    #pygame caption
    pygame.display.set_caption("Pygame Template")

    #debug: print atributes of each card in each columns 
    for column in row:
        for card in column.contents:
            print(str(card.value) + str(card.suit) + str(card.is_face_up) + str(card.image))
        print("\n")

    for card in deck_main.contents:
        print(str(card.value) + str(card.suit) + str(card.is_face_up) + str(card.image))

def display_row():
    from setting import get_x_offset, Y_OFFSET
    from obj import row, screen
    x = 0
    y = 0
    for column in row:
        y = 0
        for card in column.contents:
            screen.blit(card.image, (x, y))
            y += Y_OFFSET
        x += get_x_offset()

def display_draw_deck():
    from setting import SCREEN_HEIGHT
    from obj import draw_deck, screen
    for card in draw_deck.contents:
        screen.blit(card.image, (0, SCREEN_HEIGHT))