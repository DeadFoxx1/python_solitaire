import setting, util, obj
import sys, pygame, asyncio


async def main():
    # game init
    util.game_init()
    util.update_screen()

    # main game loop
    while True:
        # checks for events and acts acis accordingly
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                util.select_card(event.pos)
                util.update_screen()
            elif event.type == pygame.VIDEORESIZE:
                util.update_card()
                util.update_screen()

        # fps control and screen refresh MUST BE RUN LAST SO DRAWN FRAMES CAN UPDATE
        obj.clock.tick(setting.FPS)
        pygame.display.flip()
        await asyncio.sleep(0)
asyncio.run(main())
