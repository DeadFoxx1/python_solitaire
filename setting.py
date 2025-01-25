FPS = 60

BG_COLOR = (92,255,92)

SCREEN_WIDTH, SCREEN_HEIGHT = (500, 800)

#how far down the cards should offset from each other in the collumn
Y_OFFSET = 50
#NOTE x_offset is not included because it is calculated differently

SUITS = ['H', 'S', 'D', 'C']

#calculate what the width of the card should be depending on the width of the screen. used to prevent distortion
def get_card_width():
    from obj import screen
    if screen.get_size()[0] / 7 >= 169:
        return 169
    else:
        return screen.get_size()[0] / 7
    # return 169

#calculate what the height of the card should be depending on the width of the screen. used to prevent distortion. left as a function even though it returns a const incase I wanted to change later
def get_card_height():
    # from obj import screen
    # return screen.get_size()[1] / 7
    return 262

#calculate a fraction of the screen width. used to offset card columns equally and depending on screen width
def get_x_offset(denominator):
    from obj import screen
    return (screen.get_size()[0]) / denominator

