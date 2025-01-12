import pygame
import sys
import setting
import obj
import utill

#game init
utill.game_init()

#main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    obj.screen.fill(setting.BG_COLOR)

    # update display
    pygame.display.flip()

    # control frame rate
    obj.clock.tick(setting.FPS)

