import pygame as pg		

 
WHITE = (255, 255, 255)		
YELLOW = (255, 183, 0)		
GREEN = (0, 255, 0)		

 
class Snake(object):
    def __init__(self, screen_height):		
        self.head = [50, (screen_height // 2) - 40]		
        self.tail = [[50, (screen_height // 2) - 40], [40, (screen_height // 2) - 40], [40, (screen_height // 2) - 40]]		
        self.radius = 5		
        self.speed = 2 * self.radius + 2		
        self.win = 0		

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

    def bump(self, control, snake):	
        once_flag = True

        for part in self.tail[1:]:		
            if ((part[0] - self.radius <= self.head[0] - self.radius <= part[0] + self.radius or		
                part[0] - self.radius <= self.head[0] + self.radius <= part[0] + self.radius) and		
                (part[1] - self.radius <= self.head[1] - self.radius <= part[1] + self.radius or		
                part[1] - self.radius <= self.head[1] + self.radius <= part[1] + self.radius)):		

                control.run = False		
                if once_flag:
                    self.win += 1
                    once_flag = False

        for part in self.tail:		
            if ((part[0] - self.radius <= snake.head[0] - self.radius <= part[0] + self.radius or		
                part[0] - self.radius <= snake.head[0] + self.radius <= part[0] + self.radius) and		
                (part[1] - self.radius <= snake.head[1] - self.radius <= part[1] + self.radius or		
                part[1] - self.radius <= snake.head[1] + self.radius <= part[1] + self.radius)):		

                control.run = False		
                if once_flag:
                    snake.win += 1
                    once_flag = False


class Snake_second(Snake):		
    def __init__(self, screen_height):		
        self.head = [50, (screen_height // 2) + 40]		
        self.tail = [[50, (screen_height // 2) + 40], [40, (screen_height // 2) + 40], [40, (screen_height // 2) + 40]]		
        self.radius = 5		
        self.speed = 2 * self.radius + 2		
        self.win = 0		

    def draw_snake(self, screen):

        for part in self.tail:
            if part == self.head:
                pg.draw.circle(screen, (73, 15, 175), (part[0], part[1]), self.radius)		
            else:
                pg.draw.circle(screen, (255, 224, 0), (part[0], part[1]), self.radius)
