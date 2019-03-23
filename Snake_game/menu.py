import pygame as pg
from button import Button
import sys
from game_cycle import game_cycle


def menu_screen(screen, screen_size, screen_colour):

    single_button = Button(200, 50, 150, 130, (169,169,169), (225, 186, 207))
    multi_button = Button(200, 50, 150, 190, (169,169,169), (225, 186, 207))
    exit_button = Button(200, 50, 150, 250, (169,169,169), (225, 186, 207))

    touched = False
    menu_screen = True
    while menu_screen:
        pg.time.delay(50)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        screen.fill(screen_colour)

        single_key = single_button.draw(screen, 'Singleplayer', 30, 17)
        multi_key = multi_button.draw(screen, 'Multiplayer', 38, 17)
        
        exit_key = exit_button.draw(screen, 'Exit', 75, 17)
        if single_key == 'done':
            return 'single'
        elif multi_key == 'done':
            return 'multi'
        elif exit_key == 'done':
            sys.exit()

        pg.display.update()
