#contaiins utilities used in game
import pygame


def game_init():
    from obj import top_row, bottom_row, deck_main, draw_deck, foundation
    #init pygame
    pygame.init()

    #pygame caption
    pygame.display.set_caption("Pygame Template")

    #debug: print atributes of each card in each columns 
    for column in top_row:
        for card in column.contents:
            print(str(card.value) + str(card.suit) + str(card.is_face_up) + str(card.image))
        print("\n")

    for column in bottom_row:
        for card in column.contents:
            print(str(card.value) + str(card.suit) + str(card.is_face_up) + str(card.image))
        print("\n")

def display_top_row():
    from setting import get_x_offset, Y_OFFSET, SCREEN_HEIGHT
    from obj import top_row, screen, draw_deck

    x = 0
    for column in top_row:
        column.display_column(x, 0, 0, Y_OFFSET)
        x += get_x_offset(7)

def display_bottom_row():
    from setting import SCREEN_HEIGHT, get_x_offset
    from obj import draw_deck, bottom_row

    x = 0
    for column in bottom_row:
        column.display_column(x, SCREEN_HEIGHT)
        x += get_x_offset(5)

    
        