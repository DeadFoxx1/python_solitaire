import game_objs
import pygame
import settings

clock = pygame.time.Clock()
screen = pygame.display.set_mode((settings.width, settings.height))

def game_init():

    #init pygame
    pygame.init()

    #pygame caption
    pygame.display.set_caption("Pygame Template")

    #debug: print atributes of each card in each columns 
    for column in game_objs.row:
        print("\n")
        for card in column.contents:
            print(str(card.value) + str(card.suit) + str(card.is_face_up))

    for card in game_objs.deck_main.contents:
        print(str(card.value) + str(card.suit) + str(card.is_face_up))