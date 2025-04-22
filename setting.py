import argparse


def get_screen_width():
    from obj import screen

    return screen.get_width()


def get_screen_height():
    from obj import screen

    return screen.get_height()


def get_card_width():
    from obj import screen

    return min(MAX_CARD_WIDTH, get_screen_width() / 7)


def get_card_height():
    return min(MAX_CARD_HEIGHT, get_screen_height() / 3)


def cards_to_draw(value):
    ivalue = int(value)
    if ivalue > 24:
        raise argparse.ArgumentTypeError(f"too many cards {value}")
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

MAX_CARD_WIDTH = 169

MAX_CARD_HEIGHT = 262

MAX_DRAWNCARD_X_OFFSET = 40


# the playing column automatically solves for this based on the amount of cards in the column
# this sets the max length of the y_offset
# NOTE: if this value is larger then the calculated offset, it means it would result in column overlap and will be ignored
MAX_Y_OFFSET = 50

SUITS = ["H", "S", "D", "C"]
