import pygame as pg
from colours import Colours


class Button(object):
    """Class for creating screen button."""

    def __init__(self, width, height, x, y, inactive_colour, active_colour):
        """Init instance.

        Arguments:
            width(int): Button's width.
            height(int): Button's height.
            x(int): Button's x coordinate.
            y(int): Button's y coordinate.
            inactive_colour(tuple): Colour, when cursor is not on the button.
            active_colour(tuple): Colour, when cursor is on the button.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.inactive_colour = inactive_colour
        self.active_colour = active_colour

    def draw(self, screen, message, text_x, text_y):
        """Draws button on screen.

        Arguments:
            screen(tuple): Screen width(int), screen height(int).
            message(str): Text on a button.
            text_x(int): Text's x coordinate.
            text_y(int): Text's y coordinate.
        """

        mouse = pg.mouse.get_pos()

        if (self.x < mouse[0] < self.x + self.width and
           self.y < mouse[1] < self.y + self.height):

            pg.draw.rect(screen, self.active_colour, (self.x, self.y,
                         self.width, self.height))

            for event in pg.event.get():
                if (event.type == pg.MOUSEBUTTONDOWN or
                   event.type == pg.MOUSEBUTTONUP):
                    return 'done'
        else:
            pg.draw.rect(screen, self.inactive_colour, (self.x, self.y,
                         self.width, self.height))

        print_text(screen, message, self.x + text_x, self.y + text_y)


def print_text(screen, message, x, y, font_colour=Colours().WHITE,
               font_type='arial', font_size=30):
    """Draws text.

    Arguments:
        screen(tuple): Screen width(int), screen height(int).
        message(str): Text on a button.
        x(int): Text's x coordinate.
        y(int): Text's y coordinate.
        font_colour(tuple): Text's colour.
        font_type(str): Font type.
        font_size(int): Font size.
    """

    font_type = pg.font.SysFont(font_type, font_size)
    text = font_type.render(message, True, font_colour)
    screen.blit(text, (x, y))
