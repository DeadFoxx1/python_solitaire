import setting
import sys
import pygame
import obj
import util

# game init
util.game_init()


def draw_screen():
    obj.screen.fill(setting.BG_COLOR)
    util.display_rows()


# main game loop
while True:
    # checks for events and acts acis accordingly
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            util.select_card(event.pos)
            draw_screen()
        elif event.type == pygame.VIDEORESIZE:
            util.update_card()
            draw_screen()

    # fps control and screen refresh MUST BE RUN LAST SO DRAWN FRAMES CAN UPDATE
    obj.clock.tick(setting.FPS)
    pygame.display.flip()
