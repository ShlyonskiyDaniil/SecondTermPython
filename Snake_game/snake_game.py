import pygame as pg
from action_control import Control
from snake import Snake
from snake_food import Food


BLACK = (0, 0, 0)

pg.init()
screen_size = (400, 400)
screen = pg.display.set_mode(screen_size)
pg.display.set_caption("Snake")


snake = Snake()
control = Control()
food = Food(screen_size)

while control.run:
    pg.time.delay(30)
    control.control(snake)

    screen.fill(BLACK)
    
    food.draw_food(screen)
    snake.draw_snake(screen)
    snake.turn(control, screen_size)
    snake.movement()
    food.was_eaten(snake, control)
    snake.bump(control)

    pg.display.update()