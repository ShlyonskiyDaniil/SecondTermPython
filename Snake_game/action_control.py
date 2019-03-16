import pygame as pg


class Control(object):
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
                    if snake.speed != 20:
                        snake.speed += 1
                else:
                    self.facing = 'left'
                    snake.speed = 2 * snake.radius + 2
                
        elif keys[pg.K_d]:
            if not self.facing == 'left':
                if self.facing == 'right':
                    if snake.speed != 20:
                        snake.speed += 1
                else:
                    self.facing = 'right'
                    snake.speed = 2 * snake.radius + 2
        elif keys[pg.K_w]:
            if not self.facing == 'down':
                if self.facing == 'up':
                    if snake.speed != 20:
                        snake.speed += 1
                else:
                    self.facing = 'up'
                    snake.speed = 2 * snake.radius + 2
        elif keys[pg.K_s]:
            if not self.facing == 'up':
                if self.facing == 'down':
                    if snake.speed != 20:
                        snake.speed += 1
                else:
                    self.facing = 'down'
                    snake.speed = 2 * snake.radius + 2
        elif keys[pg.K_SPACE]:
            if snake.speed != 20:
                snake.speed += 1
