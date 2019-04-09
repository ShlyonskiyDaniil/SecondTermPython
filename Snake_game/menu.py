import pygame as pg
from button import Button
import sys
from game_cycle import game_cycle
from colours import Colours


def menu_screen(screen, screen_size, screen_colour):
    """Defines a menu screen view.

    Arguments:
        screen: Game dislpay.
        screen_size(tuple): Screen_widht(int), screen height(int).
        screen_colour(tuple): Screen_colour(RGB).
    """

    single_button = Button(200, 50, 150, 130, Colours().GREY, Colours().PINK)
    multi_button = Button(200, 50, 150, 190, Colours().GREY, Colours().PINK)
    exit_button = Button(200, 50, 150, 250, Colours().GREY, Colours().PINK)

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
