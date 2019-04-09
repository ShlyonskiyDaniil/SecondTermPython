import pygame as pg
from colours import Colours


class Snake(object):
    """Class for creating first snake."""

    def __init__(self, screen_height):
        """Init instance.

        Arguments:
            screen_height(int): A height of the game screen.
        """

        self.head = [50, (screen_height // 2) - 40]
        self.tail = [[50, (screen_height // 2) - 40],
                     [40, (screen_height // 2) - 40],
                     [40, (screen_height // 2) - 40]]
        self.radius = 5
        self.speed = 2 * self.radius + 2
        self.win = 0
        self.was_eaten = False

    def turn(self, control, screen_size):
        """Defines sanke action, while turning.

        Arguments:
            control(Control): An instance of class Control.
            screen_size(tuple): Screen_width(int), screen_height(int).
        """

        if control.facing == 'right':
            self.head[0] += self.speed
            if self.head[0] > screen_size[0]:
                self.head[0] = 0

        elif control.facing == 'left':
            self.head[0] -= self.speed
            if self.head[0] < 0:
                self.head[0] = screen_size[0]

        elif control.facing == 'down':
            self.head[1] += self.speed
            if self.head[1] > screen_size[1]:
                self.head[1] = 0

        elif control.facing == 'up':
            self.head[1] -= self.speed
            if self.head[1] < 0:
                self.head[1] = screen_size[1]

    def movement(self):
        """It is responsible for snake_snake movement."""

        self.tail.insert(0, list(self.head))
        self.tail.pop()

    def draw_snake(self, screen):
        """Draws first snake on the screen.

        Arguments:
            screen: Game display.
        """

        for part in self.tail:
            if part == self.head:
                    pg.draw.circle(screen, Colours().YELLOW,
                                   (part[0], part[1]),
                                   self.radius)
            else:
                pg.draw.circle(screen,
                               Colours().GREEN,
                               (part[0], part[1]),
                               self.radius)

    def bump(self, control, snake=None):
        """Defines situations, when snake was bumped.

        Arguments:
            control(Control): An instance of class Control.
            snake(Snake): An instance of class Snake.
        """

        once_flag = True

        for part in self.tail[1:]:
            if ((part[0] - self.radius <=
                 self.head[0] - self.radius <= part[0] + self.radius or
                 part[0] - self.radius <=
                 self.head[0] + self.radius <= part[0] + self.radius) and
                (part[1] - self.radius <=
                 self.head[1] - self.radius <= part[1] + self.radius or
                 part[1] - self.radius <=
                 self.head[1] + self.radius <= part[1] + self.radius)):

                control.run = False
                if once_flag:
                    self.win += 1
                    once_flag = False

        if snake is not None:
            for part in self.tail:
                if ((part[0] - self.radius <=
                     snake.head[0] - self.radius <= part[0] + self.radius or
                     part[0] - self.radius <=
                     snake.head[0] + self.radius <= part[0] + self.radius) and
                    (part[1] - self.radius <=
                     snake.head[1] - self.radius <= part[1] + self.radius or
                     part[1] - self.radius <=
                     snake.head[1] + self.radius <= part[1] + self.radius)):

                    control.run = False
                    if once_flag:
                        snake.win += 1
                        once_flag = False

    def grow(self, control):
        """Defines situations, when snake has eaten food."""

        if self.was_eaten:
            last_part = self.tail[-1]
            prelast_part = self.tail[-2]
            facing = control.facing

            if last_part[0] == prelast_part[0]:
                if last_part[1] < prelast_part[1]:
                    self.tail.append([last_part[0], last_part[1] - self.speed])
                elif last_part[1] > prelast_part[1]:
                    self.tail.append([last_part[0], last_part[1] + self.speed])

            elif last_part[1] == prelast_part[1]:
                if last_part[0] < prelast_part[0]:
                    self.tail.append([last_part[0] - self.speed, last_part[1]])
                elif last_part[0] > prelast_part[0]:
                    self.tail.append([last_part[0] + self.speed, last_part[1]])

            self.was_eaten = False


class Snake_second(Snake):
    """Class for creation second snake."""
    def __init__(self, screen_height):
        """Init instance.

        Arguments:
            screen_height(int): A height of the game screen.
        """

        self.head = [50, (screen_height // 2) + 40]
        self.tail = [[50, (screen_height // 2) + 40],
                     [40, (screen_height // 2) + 40],
                     [40, (screen_height // 2) + 40]]
        self.radius = 5
        self.speed = 2 * self.radius + 2
        self.win = 0
        self.was_eaten = False

    def draw_snake(self, screen):
        """Draws second snake on the screen.

        Arguments:
            screen: Game display.
        """

        for part in self.tail:
            if part == self.head:
                pg.draw.circle(screen, (73, 15, 175),
                               (part[0], part[1]), self.radius)
            else:
                pg.draw.circle(screen, (255, 224, 0),
                               (part[0], part[1]), self.radius)
