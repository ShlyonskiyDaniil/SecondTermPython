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
game_time = 15               # Game time in seconds;
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

game = True
while game:
    first_snake = Snake(screen_size[1])
    second_snake = Snake_second(screen_size[1])
    control_first_snake = Control_first_snake()
    control_second_snake = Control_second_snake()
    first_food = Food(screen_size)
    second_food = Food(screen_size)
    time_flag = [True, ]

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
