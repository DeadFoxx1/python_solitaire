import json
import pygame
import os, sys

# This is some bull with pyinstaller 
"""https://stackoverflow.com/questions/61881256/bundling-python-with-pyinstaller-onefile-add-data-not-working"""
try:
   wd = sys._MEIPASS
except AttributeError:
   wd = os.getcwd()

sprite_sheet = pygame.image.load(os.path.join(wd,"assets/sheet.png")).convert_alpha()

with open(os.path.join(wd,"assets/sheet.json"), "r") as file:
    data = json.load(file)


def get_image(id):
    x = data[f"{id}"][0]
    y = data[f"{id}"][1]
    sprite_width = data[f"{id}"][2]
    sprite_height = data[f"{id}"][3]

    sprite_rect = pygame.Rect(x, y, sprite_width, sprite_height)

    sprite_image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
    sprite_image.blit(sprite_sheet, (0, 0), sprite_rect)

    return sprite_image
