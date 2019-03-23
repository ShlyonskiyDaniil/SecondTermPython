import pygame as pg		

 
class Control_first_snake(object):		
    def __init__(self):		
        self.run = True		
        self.facing = 'right'		

    def control(self, snake):		
        for event in pg.event.get():		
            if event.type == pg.QUIT:		
                self.run = False		

        keys = pg.key.get_pressed()		
        if keys[pg.K_a]:		
            if not self.facing == 'right':		
                if self.facing == 'left':		
                    if snake.speed != 15:		
                        snake.speed += 1		
                else:		
                    self.facing = 'left'		
                    snake.speed = 2 * snake.radius + 1		

        elif keys[pg.K_d]:		
            if not self.facing == 'left':		
                if self.facing == 'right':		
                    if snake.speed != 15:		
                        snake.speed += 1		
                else:		
                    self.facing = 'right'		
                    snake.speed = 2 * snake.radius + 2		
        elif keys[pg.K_w]:		
            if not self.facing == 'down':		
                if self.facing == 'up':		
                    if snake.speed != 15:		
                        snake.speed += 1		
                else:		
                    self.facing = 'up'		
                    snake.speed = 2 * snake.radius + 2		
        elif keys[pg.K_s]:		
            if not self.facing == 'up':		
                if self.facing == 'down':		
                    if snake.speed != 15:		
                        snake.speed += 1		
                else:		
                    self.facing = 'down'		
                    snake.speed = 2 * snake.radius + 2		
        elif keys[pg.K_SPACE]:		
            snake.tail.append([-1 * snake.radius, -1 * snake.radius])		

class Control_second_snake(Control_first_snake):		
    def control(self, snake):		
        for event in pg.event.get():		
            if event.type == pg.QUIT:		
                self.run = False		

        keys = pg.key.get_pressed()		
        if keys[pg.K_j]:		
            if not self.facing == 'right':		
                if self.facing == 'left':		
                    if snake.speed != 15:		
                        snake.speed += 1		
                else:		
                    self.facing = 'left'		
                    snake.speed = 2 * snake.radius + 1		

        elif keys[pg.K_l]:		
            if not self.facing == 'left':		
                if self.facing == 'right':		
                    if snake.speed != 15:		
                        snake.speed += 1		
                else:		
                    self.facing = 'right'		
                    snake.speed = 2 * snake.radius + 2		
        elif keys[pg.K_i]:		
            if not self.facing == 'down':		
                if self.facing == 'up':		
                    if snake.speed != 15:		
                        snake.speed += 1		
                else:		
                    self.facing = 'up'		
                    snake.speed = 2 * snake.radius + 2		
        elif keys[pg.K_k]:		
            if not self.facing == 'up':		
                if self.facing == 'down':		
                    if snake.speed != 15:		
                        snake.speed += 1		
                else:		
                    self.facing = 'down'		
                    snake.speed = 2 * snake.radius + 2		
        elif keys[pg.K_SPACE]:		
            snake.tail.append([-1 * snake.radius, -1 * snake.radius])
