import os
import pygame

class Card:

    def __init__(self, suit: "str: must be a suit as defined in setting.SUITS", value: "int: must be either 1-13 or Str: joker", is_face_up: bool, foundation: "optional" = False):
        #NOTE: all vars with "_" are not ment to be used outside of class but because python does not allow for private vars, is notated with an _. look up "getter and setter oop" to learn more
        self.__suit = suit
        self.__value = value
        self.__is_face_up = is_face_up
        self.foundation = foundation
        
    #getter: gets stored value
    @property
    def suit(self):
        return self.__suit

    #setter
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

    @value.setter
    def value(self, value: int):
        if value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
            self.__value = value
        elif self.foundation:
            self.__value = 0
        else:
            raise ValueError("card must be between 1-13")

    @property
    def is_face_up(self):
        return self.__is_face_up

    @is_face_up.setter
    def is_face_up(self, is_face_up):
        if isinstance(is_face_up, bool):
            self.__is_face_up = is_face_up
        else:
            raise ValueError("must be a boolean")

    @property
    def image(self):
        from setting import get_card_height, get_card_width
        if self.foundation:
            image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', f'assets/{self.__suit}_empty.png'))
            return pygame.transform.scale(image, (get_card_width(), get_card_height()))
        elif self.__is_face_up == False:
            image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', f'assets/red_back_blank.png'))
            return pygame.transform.scale(image, (get_card_width(),get_card_height()))
        else:
            image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', f'assets/{self.__value}{self.__suit}.png'))
            return pygame.transform.scale(image, (get_card_width(),get_card_height()))