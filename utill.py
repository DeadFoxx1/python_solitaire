import pygame

card_cache = None

#run at creation of game but will not loop
def game_init():
    from obj import top_row, bottom_row
    #init pygame
    pygame.init()

    #pygame caption
    pygame.display.set_caption("Pygame Template")

    #debug: print attributes of each card in each column 
    for column in top_row.contents:
        for card in column.contents:
            print(card)
        print("\n")

    for column in bottom_row.contents:
        for card in column.contents:
            print(card)
        print("\n")

def display_rows():
    from obj import bottom_row, top_row
    bottom_row.display()
    top_row.display()

def clear_select_cards(selected_card):
    global card_cache
    selected_card[1].is_selected = False
    card_cache[1].is_selected = False
    card_cache = None

def select_card(pos: "event.pos"):
    global card_cache
    from obj import top_row, bottom_row

    if (result := bottom_row.select_card(pos)) != None:
        selected_card = result
    elif (result := top_row.select_card(pos)) != None:
        selected_card = result
    else:
        card_cache = None
        return

    if card_cache != None:
        move_card(selected_card)
        clear_select_cards(selected_card)
    else:
        card_cache = selected_card

def move_card(card_destination):
    global card_cache
    cards_to_move = card_cache[0].contents[card_cache[0].contents.index(card_cache[1]):]
        #if the color is opposite and the destination is on more 
        #OR if the destination is a foundation, the suit is the same, and the value is one more then in the foundation, 
        #move
    if (card_destination[0].contents[-1].color != card_cache[1].color and \
        card_destination[0].contents[-1].value == card_cache[1].value + 1) or \
        (card_destination[0].contents[0].value == 0 and \
        card_destination[0].contents[-1].value == card_cache[1].value - 1 and \
        card_destination[0].contents[-1].suit == card_cache[1].suit):

        print(f"move {card_cache[1]} to {card_destination[1]}")
        for card in cards_to_move:
            card_cache[0].contents.remove(card)
            card_destination[0].contents.append(card)
        if len(card_cache[0].contents) != 0:
            card_cache[0].contents[-1].is_face_up = True
    else:
        print("invalid move")
    
def update_card():
    from obj import top_row, bottom_row
    top_row.update_card()
    bottom_row.update_card()