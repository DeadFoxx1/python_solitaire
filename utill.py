#contaiins utilities used in game
import pygame


def game_init():
    from obj import row, deck_main, draw_deck
    #init pygame
    pygame.init()

    #pygame caption
    pygame.display.set_caption("Pygame Template")

    #debug: print atributes of each card in each columns 
    for column in row:
        for card in column.contents:
            print(str(card.value) + str(card.suit) + str(card.is_face_up) + str(card.image))
        print("\n")

    for card in draw_deck.contents:
        print(str(card.value) + str(card.suit) + str(card.is_face_up) + str(card.image))

def display_cards():
    from setting import get_x_offset, Y_OFFSET, SCREEN_HEIGHT
    from obj import row, screen, draw_deck
    x = 0
    for column in row:
        column.display_column(x, 0, 0, Y_OFFSET)
        x += get_x_offset()
    draw_deck.display_column(0, SCREEN_HEIGHT)


