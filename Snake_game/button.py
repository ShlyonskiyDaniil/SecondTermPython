import pygame as pg


class Button(object):
    def __init__(self, width, height, x, y, inactive_colour, active_colour):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.inactive_colour = inactive_colour
        self.active_colour = active_colour

    def draw(self, screen, message, text_x, text_y):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        if (self.x < mouse[0] < self.x + self.width and
            self.y < mouse[1] < self.y + self.height):

            pg.draw.rect(screen, self.active_colour, (self.x, self.y, self.width, self.height))

            if click[0] == 1:
                    pg.time.delay(30)
                    return 'done'
        else:
            pg.draw.rect(screen, self.inactive_colour, (self.x, self.y, self.width, self.height))

        print_text(screen, message, self.x + text_x, self.y + text_y)

def print_text(screen, message, x, y, font_colour=(255, 255, 255), font_type='arial', font_size=30):
    font_type = pg.font.SysFont(font_type, font_size)
    text = font_type.render(message, True, font_colour)
    screen.blit(text, (x, y))
