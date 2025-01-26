import os
import pygame

class Card:
    def __init__(self, suit: "str: must be a suit as defined in setting.SUITS", value: "int: must be either 0-13 or Str: joker. If 0, will be a foundation", is_face_up: bool):
        self.suit = suit
        self.value = value
        self.is_face_up = is_face_up
        self.load_image()
        self.is_selected = False
        
    def __str__(self):
        return f"{self.value}{self.suit}{self.is_face_up}"

    @property
    def suit(self):
        return self.__suit

    @suit.setter
    def suit(self, suit: "Must be defined in settings"):
        from setting import SUITS
        if suit in SUITS:
            self.__suit = suit
        else:
            raise ValueError("Suit Must be defined in settings")

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
            self.__value = value
        else:
            raise ValueError("Must be either 0-13. If 0, will be a foundation")

    @property
    def is_face_up(self):
        return self.__is_face_up

    @is_face_up.setter
    def is_face_up(self, is_face_up: bool):
        self.__is_face_up = is_face_up
        self.load_image()

    @property
    def is_selected(self):
        return self.__is_selected
    
    @is_selected.setter
    def is_selected(self, bool):
        if bool:
            self.yellow_highlight.set_alpha(128)
        else:
            self.yellow_highlight.set_alpha(0)
        self.__is_selected = bool

    @property
    def color(self):
        if self.suit in ["H", "D"]:
            return "red"
        else:
            return "black"

    def load_image(self):
        """updates the card image based on the attributes of the card.
        if face down show back of card
        if face up show card based on suit and num
        if value = 0, show foundation card
        also updates card size, yellow highlight size, and rect onj size"""
        from setting import get_card_height, get_card_width
        if self.value == 0:
            image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', f'assets/{self.suit}_empty.png'))
        elif self.is_face_up == False:
            image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', f'assets/red_back_blank.png'))
        else:
            image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', f'assets/{self.value}{self.suit}.png'))

        self.image = pygame.transform.scale(image, (get_card_width(), get_card_height()))
        self.yellow_highlight =  pygame.Surface(self.image.get_size())
        self.yellow_highlight.fill((255, 255, 0))
        self.yellow_highlight.set_alpha(0)
        self.rect = self.image.get_rect()

    def display(self, x, y):
        """displays the card at given cords"""
        from obj import screen
        screen.blit(self.image, (x, y))
        screen.blit(self.yellow_highlight, (x, y))
        self.rect.topleft = (x, y)
