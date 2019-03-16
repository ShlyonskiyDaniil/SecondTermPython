import pygame as pg


WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

class Snake(object):
    def __init__(self):
        self.head = [50, 50]
        self.tail = [[50, 50], [43, 50]]
        self.radius = 4
        self.speed = 2 * self.radius + 2

    def turn(self, control, screen_size):
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
        self.tail.insert(0, list(self.head))
        self.tail.pop()

    def draw_snake(self, screen):
        for part in self.tail:
            if part == self.head:
                pg.draw.circle(screen, YELLOW, (part[0], part[1]), self.radius)
            else:
                pg.draw.circle(screen, GREEN, (part[0], part[1]), self.radius)

    def bump(self, control):
        for part in self.tail[1:]:
            if ((part[0] - self.radius <= self.head[0] - self.radius <= part[0] + self.radius or
                 part[0] - self.radius <= self.head[0] + self.radius <= part[0] + self.radius) and
                (part[1] - self.radius <= self.head[1] - self.radius <= part[1] + self.radius or
                 part[1] - self.radius <= self.head[1] + self.radius <= part[1] + self.radius)):

                print(f'head: {self.head[0]}, {self.head[1]}')
                print(f'{part[0]}, {part[1]}')
                control.run = False
