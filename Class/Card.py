import os
import pygame

class Card:

    def __init__(self, suit: "str: must be a suit as defined in setting.SUITS", value: "int: must be either 0-13 or Str: joker. If 0, will be a foundation", is_face_up: bool):
        self.suit = suit
        self.value = value
        self.is_face_up = is_face_up
        self.load_image()
        
    def __str__(self):
        return f"{self.value}{self.suit}{self.is_face_up}{self.image}"

    @property
    def suit(self):
        return self.__suit

    @suit.setter
    #check if given suit is valid as defined in setting.SUITS and gives an error if not. If it is, define the card's suit as passed in
    def suit(self, suit):
        from setting import SUITS
        if suit in SUITS:
            self.__suit = suit
        else:
            raise ValueError("Suit must be one of ['H', 'S', 'D', 'C']")

    @property
    def value(self):
        return self.__value

    #check if given value is valid and gives an error if not. If it is, define the card's value as passed in. 0 is for foundation
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
    def is_face_up(self, is_face_up):
        if isinstance(is_face_up, bool):
            self.__is_face_up = is_face_up
            self.load_image()
        else:
            raise ValueError("must be a boolean")

    def load_image(self):
        from setting import get_card_height, get_card_width
        if self.value == 0:
            image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', f'assets/{self.__suit}_empty.png'))
        elif self.__is_face_up == False:
            image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', f'assets/red_back_blank.png'))
        else:
            image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', f'assets/{self.__value}{self.__suit}.png'))

        self.__image = pygame.transform.scale(image, (get_card_width(), get_card_height()))

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, cord: tuple):
        self.__rect = self.image.get_rect(topleft=cord)