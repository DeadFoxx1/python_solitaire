import argparse


def cards_to_draw(value):
    ivalue = int(value)
    if ivalue > 24:
        raise argparse.ArgumentTypeError(f"not enough cards {value}")
    return ivalue


parser = argparse.ArgumentParser()
parser.add_argument(
    "-d", "--debug", type=bool, default=False, help="enables debug output"
)
parser.add_argument(
    "-c",
    "--cardstodraw",
    type=cards_to_draw,
    default=3,
    help="number of cards to draw at a time (must be less then 24)",
)

DEBUG = parser.parse_args().debug

CARDS_TO_DRAW = parser.parse_args().cardstodraw

FPS = 60

BG_COLOR = (33, 148, 0)

SCREEN_WIDTH, SCREEN_HEIGHT = (500, 500)

CARD_HEIGHT = 262

# how far down the cards should offset from each other in the column
Y_OFFSET = 50

SUITS = ["H", "S", "D", "C"]


# calculate what the width of the card should be depending on the width of the screen. used to prevent distortion
def get_card_width():
    from obj import screen

    if screen.get_size()[0] / 7 >= 169:
        return 169
    else:
        return screen.get_size()[0] / 7


# calculate a fraction of the screen width. used to offset card columns equally and depending on screen width
def get_x_offset(denominator):
    from obj import screen

    return (screen.get_size()[0]) / denominator
