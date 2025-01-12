import utill
import setting
import obj
import pygame
import sys

#game init
utill.game_init()

#main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # update display
    pygame.display.flip()

    # control frame rate
    obj.clock.tick(setting.FPS)