#contaiins utilities used in game
import pygame

#run at creation of Game but will not loop
def game_init():
    from obj import top_row, bottom_row
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

#iterate through the columns in the top row and add the necessary offset to each card and each column
def display_top_row():
    from setting import get_x_offset, Y_OFFSET, SCREEN_HEIGHT
    from obj import top_row

    x = 0
    for column in top_row:
        column.display_column(x, 0, 0, Y_OFFSET)
        x += get_x_offset(7)

#iterate through the columns in the bottom row and add the necessary offset to each (x)
def display_bottom_row():
    from setting import SCREEN_HEIGHT, get_x_offset
    from obj import bottom_row

    x = 0
    for column in bottom_row:
        column.display_column(x, SCREEN_HEIGHT)
        x += get_x_offset(5)

def select_card(pos: "event.pos"):
    from obj import top_row
    for column in top_row:
        for card in reversed(column.contents):
            if card.rect.collidepoint(pos):
                print(f"card {card.value}{card.suit} selected!")
                break