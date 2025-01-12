FPS = 60

BG_COLOR = (48,255,33)

SCREEN_WIDTH, SCREEN_HEIGHT = (500, 800)

def get_CARD_WIDTH():
    from obj import screen
    return int(screen.get_size()[0] / 7)


def get_CARD_HEIGHT():
    from obj import screen
    return int(screen.get_size()[1] / 7)

CARD_WIDTH, CARD_HEIGHT = get_CARD_WIDTH(), get_CARD_HEIGHT