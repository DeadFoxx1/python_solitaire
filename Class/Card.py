import os
import pygame
import setting

class Card:

    def __init__(self, suit: str, value: int, is_face_up: bool):
        self._suit = None
        self._value = None
        self._is_face_up = None
        self.suit = suit
        self.value = value
        self.is_face_up = is_face_up
    
    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ['H', 'S', 'D', 'C']:
            self._suit = suit
        else:
            raise ValueError("Suit must be one of 'h', 's', 'd', or 'c'.")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: int):
        if value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, "joker"]:
            self._value = value
        else:
            raise ValueError("card must be between 1-13 or a joker")

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
        if self.is_face_up == False:
            image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', f'assets/red_back_blank.png'))
            return pygame.transform.scale(image, (setting.get_CARD_WIDTH(), setting.get_CARD_HEIGHT()))
        else:
            image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', f'assets/{self._value}{self._suit}.png'))
            return pygame.transform.scale(image, (setting.get_CARD_WIDTH(), setting.get_CARD_HEIGHT()))