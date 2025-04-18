import json
import pygame

sprite_sheet = pygame.image.load("sheet.png").convert_alpha()

with open("sheet.json", "r") as file:
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
