import pygame

#run at creation of Game but will not loop
def game_init():
    from obj import top_row, bottom_row
    #init pygame
    pygame.init()

    #pygame caption
    pygame.display.set_caption("Pygame Template")

    #debug: print atributes of each card in each column 
    for column in top_row.contents:
        for card in column.contents:
            print(card)
        print("\n")

    for column in bottom_row.contents:
        for card in column.contents:
            print(card)
        print("\n")

#iterate through the columns in the bottom row and add the necessary offset to each (x)
def display_rows():
    from obj import bottom_row, top_row
    bottom_row.display()
    top_row.display()

def select_card(pos: "event.pos"):
    from obj import top_row, bottom_row
    top_row.select_card(pos)
    bottom_row.select_card(pos)

def update_card():
    from obj import top_row, bottom_row
    top_row.update_card()
    bottom_row.update_card()
