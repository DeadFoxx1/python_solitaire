FPS = 60

BG_COLOR = (48,255,33)

SCREEN_WIDTH, SCREEN_HEIGHT = (500, 800)

def get_card_width():
    from obj import screen
    if screen.get_size()[0] / 7 >= 169:
        return 169
    else:
        return screen.get_size()[0] / 7
    # return 169

def get_card_height():
    # from obj import screen
    # return screen.get_size()[1] / 7
    return 262

def get_x_offset(denominator):
    from obj import screen
    return (screen.get_size()[0]) / denominator

Y_OFFSET = 50