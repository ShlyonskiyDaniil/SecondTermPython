import pygame as pg
from action_control import Control, Control_second_snake
from snake import Snake, Snake_second
from snake_food import Food
from time import time
from result import game_result

# Players' parameters:
player_wasd = 'Player1'      # First player name;
player_ijkl = 'Player2'      # Second player name;
game_time = 5                # Game time in seconds;
screen_size = (400, 400)     # Screen size.
# End of players' parameters.

BLACK = (0, 0, 0)

pg.init()
screen = pg.display.set_mode(screen_size)
pg.display.set_caption("Snake forever")


first_snake = Snake(screen_size[1])
second_snake = Snake_second(screen_size[1])
control = Control()
control_second_snake = Control_second_snake()
food = Food(screen_size)

timer = time()
time_flag = True
while control.run and control_second_snake.run:
    if time() - timer > game_time:
        time_flag = False
        control.run = False

    pg.time.delay(50)
    control.control(first_snake)
    control_second_snake.control(second_snake)

    screen.fill(BLACK)
    
    food.draw_food(screen, first_snake)
    food.draw_food(screen, second_snake)

    first_snake.draw_snake(screen)
    first_snake.turn(control, screen_size)
    first_snake.movement()

    second_snake.draw_snake(screen)
    second_snake.turn(control_second_snake, screen_size)
    second_snake.movement()

    food.was_eaten(first_snake, control)
    food.was_eaten(second_snake, control_second_snake)

    first_snake.bump(control, second_snake)
    second_snake.bump(control_second_snake, first_snake)

    pg.display.update()

game_result(first_snake, second_snake, player_wasd, player_ijkl, time_flag)
