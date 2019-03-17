import pygame as pg		
from random import randint		
from snake import Snake		

 
WHITE = (255, 255, 255)		
RED = (255, 0, 0)		

class Food(object):		
    def __init__(self, screen_size):		
        self.x = screen_size[0] // 2		
        self.y = screen_size[1] // 2		
        self.radius = 6		
        self.screen_size = screen_size		
        self.is_possible = False		


    def draw_food(self, screen, snake):		

        for part in snake.tail:		
            if not (self.x - self.radius <= part[0] + snake.radius <= self.x + self.radius or 		
                    self.x - self.radius <= part[0] - snake.radius <= self.x + self.radius or		
                    self.y - self.radius <= part[1] + snake.radius <= self.y + self.radius or		
                    self.y - self.radius <= part[1] - snake.radius <= self.y + self.radius):		

                self.is_possible = True		

        if self.is_possible:		
            pg.draw.circle(screen, RED, (self.x, self.y), self.radius)		
        else:		
            self.x = randint(self.radius, self.screen_size[0] - self.radius)		
            self.y = randint(self.radius, self.screen_size[1] - self.radius)		


    def was_eaten(self, snake, control):		
# Checking, whether food was eaten.		
        if ((self.x - self.radius <= snake.head[0] - snake.radius <= self.x + self.radius or		
            self.x - self.radius <= snake.head[0] + snake.radius <= self.x + self.radius) and		
            (self.y - self.radius <= snake.head[1] - snake.radius <= self.y + self.radius or		
            self.y - self.radius <= snake.head[1] + snake.radius <= self.y + self.radius)):		

# If food was eaten, old food have to be deleted, and have to be appeared.		
            self.x = randint(self.radius, self.screen_size[0] - self.radius)		
            self.y = randint(self.radius, self.screen_size[1] - self.radius)		
            self.is_possible = False		

# If food was eaten, snake have tobecome longer.		
            last_part = snake.tail[-1]		
            prelast_part = snake.tail[-2]		
            facing = control.facing		

            if last_part[0] == prelast_part[0]:		
                if last_part[1] < prelast_part[1]:		
                    snake.tail.append([last_part[0], last_part[1] - 11])		
                elif last_part[1] > prelast_part[1]:		
                    snake.tail.append([last_part[0], last_part[1] + 11])		

            elif last_part[1] == prelast_part[1]:		
                if last_part[0] < prelast_part[0]:		
                    snake.tail.append([last_part[0] - 11, last_part[1]])		
                elif last_part[0] > prelast_part[0]:		
                    snake.tail.append([last_part[0], last_part[1]])		
