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


    utill.display_top_row()
    utill.display_bottom_row()


    obj.clock.tick(setting.FPS)
    pygame.display.flip()