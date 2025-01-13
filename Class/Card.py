import os
import pygame

class Card:

    def __init__(self, suit: str, value: int, is_face_up: bool, foundation: "optional" = False):
        self._suit = None
        self._value = None
        self._is_face_up = None
        self.foundation = foundation
        self.suit = suit
        self.value = value
        self.is_face_up = is_face_up
        
    
    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        from setting import SUITS
        if suit in SUITS:
            self._suit = suit
        else:
            raise ValueError("Suit must be one of ['H', 'S', 'D', 'C']")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: int):
        if value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
            self._value = value
        elif self.foundation:
            self._value = 0
        else:
            raise ValueError("card must be between 1-13")

    @property
    def is_face_up(self):
        return self._is_face_up

    @is_face_up.setter
    def is_face_up(self, is_face_up):
        if isinstance(is_face_up, bool):
            self._is_face_up = is_face_up
        else:
            raise ValueError("must be a boolean")

    @property
    def image(self):
        from setting import get_card_height, get_card_width
        if self.foundation:
            image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', f'assets/{self._suit}_empty.png'))
            return pygame.transform.scale(image, (get_card_width(), get_card_height()))
        elif self._is_face_up == False:
            image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', f'assets/red_back_blank.png'))
            return pygame.transform.scale(image, (get_card_width(),get_card_height()))
        else:
            image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', f'assets/{self._value}{self._suit}.png'))
            return pygame.transform.scale(image, (get_card_width(),get_card_height()))