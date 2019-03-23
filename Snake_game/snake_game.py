import pygame as pg
from action_control import Control_first_snake, Control_second_snake
from snake import Snake, Snake_second
from snake_food import Food
from time import time
from result import multi_result_screen, single_result_screen
from menu import menu_screen
from game_cycle import game_cycle


# Players' parameters:
player_wasd = 'Vovka'      # First player name;
player_ijkl = 'Vladka'      # Second player name;
game_time = 3               # Game time in seconds;
# End of players' parameters.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen_size = (520, 500) 

pg.init()
screen = pg.display.set_mode(screen_size)
pg.display.set_caption("Snake forever")
delay = 50


first_snake = Snake(screen_size[1])
second_snake = Snake_second(screen_size[1])
control_first_snake = Control_first_snake()
control_second_snake = Control_second_snake()
first_food = Food(screen_size)
second_food = Food(screen_size)

time_flag = [True,]

# menu
game = True
while game:
    first_snake = Snake(screen_size[1])
    second_snake = Snake_second(screen_size[1])
    control_first_snake = Control_first_snake()
    control_second_snake = Control_second_snake()
    first_food = Food(screen_size)
    second_food = Food(screen_size)
    time_flag = [True,]

    player_quantity = menu_screen(screen, screen_size, BLACK)
    game_cycle(screen, screen_size, delay, 
               first_snake, second_snake,
               control_first_snake,
               control_second_snake,
               first_food, second_food,
               game_time, time_flag,
               player_quantity)
    if player_quantity == 'multi':
        multi_result_screen(screen, first_snake, 
                    second_snake, first_food, 
                    second_food, player_wasd,
                    player_ijkl, time_flag)
    elif player_quantity == 'single':
        single_result_screen(screen, first_snake, 
                            first_food, player_wasd,
                            time_flag)
# game_result(first_snake, second_snake, player_wasd, player_ijkl, time_flag)



# timer = time()
# while control_first_snake.run and control_second_snake.run:
#     if time() - timer > game_time:
#         time_flag = False
#         control_first_snake.run = False

#     if time() - timer > game_time // 2:
#         pg.time.delay(delay - 30)
#     else:
#         pg.time.delay(delay)

#     screen.fill(BLACK)

#     control_first_snake.control(first_snake)
#     control_second_snake.control(second_snake)

#     first_snake.draw_snake(screen)
#     first_snake.turn(control_first_snake, screen_size)
#     first_snake.movement()

#     second_snake.draw_snake(screen)
#     second_snake.turn(control_second_snake, screen_size)
#     second_snake.movement()

#     if time() - timer < game_time // 2:
#         second_food.was_eaten(first_snake, control_first_snake)
#         second_food.was_eaten(second_snake, control_second_snake)

#         second_food.draw_food(screen, first_snake)
#         second_food.draw_food(screen, second_snake)

#     first_food.was_eaten(first_snake, control_first_snake)
#     first_food.was_eaten(second_snake, control_second_snake)

#     first_food.draw_food(screen, first_snake)
#     first_food.draw_food(screen, second_snake)

#     first_snake.bump(control_first_snake, second_snake)
#     second_snake.bump(control_second_snake, first_snake)

#     pg.display.update()