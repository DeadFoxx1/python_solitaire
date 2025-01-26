import pygame

card_cache = None

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

    top_row_selected_card = top_row.select_card(pos)
    bottom_row_selected_card = bottom_row.select_card(pos)

    if (card_cache != None) and (top_row_selected_card or bottom_row_selected_card != None):
        move_card(top_row_selected_card, bottom_row_selected_card)
    else:
        cache_card(top_row_selected_card, bottom_row_selected_card)

def cache_card(top_row_selected_card, bottom_row_selected_card): 
    global card_cache  

    if bottom_row_selected_card != None:
        card_cache = bottom_row_selected_card
        print(card_cache[1])

    elif top_row_selected_card != None:
        card_cache = top_row_selected_card
        print(card_cache[1])

    else:
        card_cache = None
        print("none selected")

def move_card(top_row_selected_card, bottom_row_selected_card):
    global card_cache
    print("move")
    card_cache = None
    
def update_card():
    from obj import top_row, bottom_row
    top_row.update_card()
    bottom_row.update_card()