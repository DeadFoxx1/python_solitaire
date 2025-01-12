import pygame
import sys
from Deck import Deck
from Column import Column

#init pygame
pygame.init()

#set screen properties
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Template")

#init clock
clock = pygame.time.Clock()
FPS = 60

#create deck and 7 columns with only last card of column face up
deck_main = Deck()
row = []
for ammount in range(8):
    row.append(Column(ammount + 1, deck_main))
    row[ammount].contents[-1].is_face_up = True


#main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # update display
    pygame.display.flip()

    # control frame rate
    clock.tick(FPS)



#debug
# for column in row:
#     print("\n")
#     for card in column.contents:
#         print(str(card.value) + str(card.suit) + str(card.is_face_up))

# for card in deck_main.contents:
#     print(str(card.value) + str(card.suit) + str(card.is_face_up))