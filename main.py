import pygame
import sys
import setting
import obj
import utill

#game init
utill.game_init()

#main game loop
while True:
    #checks is the window closed and ends the program accordingly
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #add green background
    obj.screen.fill(setting.BG_COLOR)

    #display cards
    utill.display_top_row()
    utill.display_bottom_row()




    #fps controll and screen refresh MUST BE RUN LAST SO DRAWN FRAMES CAN UPDATE
    obj.clock.tick(setting.FPS)
    pygame.display.flip()