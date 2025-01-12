#contaiins utilities used in game
import setting
import obj
import pygame


def game_init():

    #init pygame
    pygame.init()

    #pygame caption
    pygame.display.set_caption("Pygame Template")

    #debug: print atributes of each card in each columns 
    for column in obj.row:
        print("\n")
        for card in column.contents:
            print(str(card.value) + str(card.suit) + str(card.is_face_up))

    for card in obj.deck_main.contents:
        print(str(card.value) + str(card.suit) + str(card.is_face_up))