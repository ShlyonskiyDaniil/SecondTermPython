import pygame as pg
from random import randint
from colours import Colours


class Food(object):
    """Class for creating food."""

    def __init__(self, screen_size):
        """Init instance.

        Arguments:
            screen_size(tuple): Screen width(int), screen height(int).
        """

        self.radius = 6
        self.screen_size = screen_size
        self.x = randint(self.radius, self.screen_size[0] - self.radius)
        self.y = randint(self.radius, self.screen_size[1] - self.radius)
        self.is_possible = False

    def draw_food(self, screen, snake):
        """Draws food on the screen.

        Arguments:
            screen: Game display.
            snake(Snake): An instance of Snake.
        """

        for part in snake.tail:
            if not (self.x - self.radius <=
                    part[0] + snake.radius <= self.x + self.radius or
                    self.x - self.radius <=
                    part[0] - snake.radius <= self.x + self.radius or
                    self.y - self.radius <=
                    part[1] + snake.radius <= self.y + self.radius or
                    self.y - self.radius <=
                    part[1] - snake.radius <= self.y + self.radius):

                self.is_possible = True

        if self.is_possible:
            pg.draw.circle(screen,
                           Colours().RED,
                           (self.x, self.y),
                           self.radius)
        else:
            self.x = randint(self.radius, self.screen_size[0] - self.radius)
            self.y = randint(self.radius, self.screen_size[1] - self.radius)

    def was_eaten(self, snake, control):
        """Defines situations, when snake eats food.

        Attributes:
            snake(Snake): An instance of Snake.
            control(Contol): An instance of Control.
        """

        if ((self.x - self.radius <=
            snake.head[0] - snake.radius <= self.x + self.radius or
            self.x - self.radius <=
            snake.head[0] + snake.radius <= self.x + self.radius) and
            (self.y - self.radius <=
            snake.head[1] - snake.radius <= self.y + self.radius or
            self.y - self.radius <=
             snake.head[1] + snake.radius <= self.y + self.radius)):

            self.x = randint(self.radius, self.screen_size[0] - self.radius)
            self.y = randint(self.radius, self.screen_size[1] - self.radius)
            self.is_possible = False
            snake.was_eaten = True
