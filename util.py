import pygame

card_cache = None


# run at creation of game but will not loop
def game_init():
    from setting import DEBUG

    if DEBUG:
        output_debug()

    # init pygame
    pygame.init()

    # pygame caption
    pygame.display.set_caption("Pygame Template")

    update_card()


def output_debug():
    from obj import top_row, bottom_row

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


def select_card(pos):
    global card_cache
    from obj import top_row, bottom_row
    from setting import DEBUG

    if (result := bottom_row.select_card(pos)) == "draw":
        if DEBUG:
            print("draw card")
        bottom_row.draw_card()
        card_cache = None
        return
    elif result != None:
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
    from setting import DEBUG

    global card_cache
    cards_to_move = card_cache[0].contents[
        card_cache[0].contents.index(card_cache[1]) :
    ]
    destination_column = card_destination[0].contents

    # if the color is opposite and the destination is one more in value
    # OR if the destination is a foundation, the suit is the same, and the value is one more then in the foundation,
    # move
    if (
        (destination_column[-1].is_face_up and card_cache[1].is_face_up)
        and (
            destination_column[-1].color != card_cache[1].color
            and destination_column[-1].value == card_cache[1].value + 1
            and card_destination[0].can_accept_cards
        )
        or (
            destination_column[0].value == 0
            and destination_column[-1].value == card_cache[1].value - 1
            and destination_column[-1].suit == card_cache[1].suit
        )
    ):

        if DEBUG:
            print(f"move {card_cache[1]} to {card_destination[1]}")
        for card in cards_to_move:
            card_cache[0].contents.remove(card)
            card_destination[0].contents.append(card)
        if len(card_cache[0].contents) != 0:
            card_cache[0].contents[-1].is_face_up = True
    else:
        if DEBUG:
            print(f"invalid move ({card_cache[1]} to {card_destination[1]})")


def update_card():
    from obj import top_row, bottom_row

    top_row.update_card()
    bottom_row.update_card()
